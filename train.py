import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Conv1D, MaxPooling1D, Flatten
import matplotlib.pyplot as plt

# Load the dataset
csv_file_path = 'data/processed/sinan/sinan.parquet'
data = pd.read_parquet(csv_file_path)

# Convert the date column to datetime format
data['DT_NOTIFIC'] = pd.to_datetime(data['DT_NOTIFIC'])

# Sort the data by ID_UNIDADE and DT_NOTIFIC
data_sorted = data.sort_values(by=['ID_UNIDADE', 'DT_NOTIFIC'])

# Drop the 'Unnamed: 0' column if present
data_sorted = data_sorted.drop(columns=['Unnamed: 0'], errors='ignore')

# Define a function to create sequences of a given length from the data
def create_sequences(data, sequence_length, features):
    sequences = []
    targets = []
    for unit in data['ID_UNIDADE'].unique():
        unit_data = data[data['ID_UNIDADE'] == unit]
        for i in range(len(unit_data) - sequence_length):
            seq = unit_data.iloc[i:i + sequence_length]
            target = unit_data.iloc[i + sequence_length]
            sequences.append(seq[features].values)
            targets.append(target['CASES'])
    return np.array(sequences), np.array(targets)

# Define the different feature sets
all_features = ['avg_sat', 'max_sat', 'min_sat', 'avg_ws', 'max_ws', 'min_ws']
sat_features = ['avg_sat', 'max_sat', 'min_sat']
ws_features = ['avg_ws', 'max_ws', 'min_ws']

# Create sequences for each feature set
sequence_length = 7
sequences_all, targets_all = create_sequences(data_sorted, sequence_length, all_features)
sequences_sat, targets_sat = create_sequences(data_sorted, sequence_length, sat_features)
sequences_ws, targets_ws = create_sequences(data_sorted, sequence_length, ws_features)

# Normalize the features for each set
scaler_all = MinMaxScaler()
scaler_sat = MinMaxScaler()
scaler_ws = MinMaxScaler()

num_sequences_all, _, num_features_all = sequences_all.shape
num_sequences_sat, _, num_features_sat = sequences_sat.shape
num_sequences_ws, _, num_features_ws = sequences_ws.shape

sequences_all_reshaped = sequences_all.reshape(-1, num_features_all)
sequences_sat_reshaped = sequences_sat.reshape(-1, num_features_sat)
sequences_ws_reshaped = sequences_ws.reshape(-1, num_features_ws)

sequences_all_normalized = scaler_all.fit_transform(sequences_all_reshaped).reshape(num_sequences_all, sequence_length, num_features_all)
sequences_sat_normalized = scaler_sat.fit_transform(sequences_sat_reshaped).reshape(num_sequences_sat, sequence_length, num_features_sat)
sequences_ws_normalized = scaler_ws.fit_transform(sequences_ws_reshaped).reshape(num_sequences_ws, sequence_length, num_features_ws)

# Determine the split point based on dates (e.g., 80% for training, 20% for testing)
split_date = data_sorted['DT_NOTIFIC'].quantile(0.8)

# Split the data into training and testing sets for each feature set based on the date
def train_test_split_by_date(sequences, targets, data, split_date):
    train_indices = data['DT_NOTIFIC'] <= split_date
    test_indices = data['DT_NOTIFIC'] > split_date
    
    X_train = sequences[train_indices[:len(sequences)]]
    y_train = targets[train_indices[:len(targets)]]
    X_test = sequences[test_indices[:len(sequences)]]
    y_test = targets[test_indices[:len(targets)]]
    
    return X_train, X_test, y_train, y_test

X_train_all, X_test_all, y_train_all, y_test_all = train_test_split_by_date(sequences_all_normalized, targets_all, data_sorted, split_date)
X_train_sat, X_test_sat, y_train_sat, y_test_sat = train_test_split_by_date(sequences_sat_normalized, targets_sat, data_sorted, split_date)
X_train_ws, X_test_ws, y_train_ws, y_test_ws = train_test_split_by_date(sequences_ws_normalized, targets_ws, data_sorted, split_date)

# Function to create and train an LSTM model
def train_lstm_model(X_train, y_train, X_test, y_test, input_shape):
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=input_shape))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    history = model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test))
    return model, history

# Function to create and train a CNN model
def train_cnn_model(X_train, y_train, X_test, y_test, input_shape):
    model = Sequential()
    model.add(Conv1D(filters=64, kernel_size=2, activation='relu', input_shape=input_shape))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    history = model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test))
    return model, history

# Train the LSTM models
model_lstm_all, history_lstm_all = train_lstm_model(X_train_all, y_train_all, X_test_all, y_test_all, (sequence_length, num_features_all))
model_lstm_sat, history_lstm_sat = train_lstm_model(X_train_sat, y_train_sat, X_test_sat, y_test_sat, (sequence_length, num_features_sat))
model_lstm_ws, history_lstm_ws = train_lstm_model(X_train_ws, y_train_ws, X_test_ws, y_test_ws, (sequence_length, num_features_ws))

# Train the CNN models
model_cnn_all, history_cnn_all = train_cnn_model(X_train_all, y_train_all, X_test_all, y_test_all, (sequence_length, num_features_all))
model_cnn_sat, history_cnn_sat = train_cnn_model(X_train_sat, y_train_sat, X_test_sat, y_test_sat, (sequence_length, num_features_sat))
model_cnn_ws, history_cnn_ws = train_cnn_model(X_train_ws, y_train_ws, X_test_ws, y_test_ws, (sequence_length, num_features_ws))

# Plot training & validation loss values for all models
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.plot(history_lstm_all.history['loss'], label='Train')
plt.plot(history_lstm_all.history['val_loss'], label='Validation')
plt.title('LSTM with All Features')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(loc='upper right')

plt.subplot(2, 3, 2)
plt.plot(history_lstm_sat.history['loss'], label='Train')
plt.plot(history_lstm_sat.history['val_loss'], label='Validation')
plt.title('LSTM with Satellite Features')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(loc='upper right')

plt.subplot(2, 3, 3)
plt.plot(history_lstm_ws.history['loss'], label='Train')
plt.plot(history_lstm_ws.history['val_loss'], label='Validation')
plt.title('LSTM with Weather Station Features')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(loc='upper right')

plt.subplot(2, 3, 4)
plt.plot(history_cnn_all.history['loss'], label='Train')
plt.plot(history_cnn_all.history['val_loss'], label='Validation')
plt.title('CNN with All Features')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(loc='upper right')

plt.subplot(2, 3, 5)
plt.plot(history_cnn_sat.history['loss'], label='Train')
plt.plot(history_cnn_sat.history['val_loss'], label='Validation')
plt.title('CNN with Satellite Features')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(loc='upper right')

plt.subplot(2, 3, 6)
plt.plot(history_cnn_ws.history['loss'], label='Train')
plt.plot(history_cnn_ws.history['val_loss'], label='Validation')
plt.title('CNN with Weather Station Features')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()
