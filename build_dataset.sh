# Activate env
source /opt/anaconda/bin/activate arboseer

# Download and process CNES Health Units data - OK
#python src/utils/download_cnes_file.py ST RJ 2401 data/raw/cnes/STRJ2401.dbc
#python src/utils/dbc_to_parquet.py data/raw/cnes/STRJ2401.dbc data/raw/cnes/STRJ2401.parquet
#python src/process_cnes_dataset.py data/raw/cnes/STRJ2401.parquet data/processed/cnes/STRJ2401.parquet

# Download and process SINAN dengue cases - OK
#python src/utils/download_sinan_file.py DENG 2023 data/raw/sinan
#python src/extract_sinan_cases.py data/raw/sinan/DENGBR23.parquet data/processed/sinan/DENGBR23.parquet --cod_uf 33

# Download inmet data - OK
#python src/utils/download_inmet_data.py -s A617 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A615 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A628 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A606 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A502 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A604 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A607 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A620 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A629 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A557 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A603 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A518 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A608 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A517 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A627 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A624 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A570 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A513 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A619 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A529 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A610 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A622 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A637 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A609 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A626 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A652 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A636 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A621 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A602 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A630 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A514 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A667 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A601 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A659 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A618 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A625 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A611 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A633 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A510 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A634 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN
#python src/utils/download_inmet_data.py -s A612 -b 2023 -e 2023 -o data/processed/inmet --api_token $INMET_API_TOKEN

# Calculate LST - OK
#python src/calculate_min_max_avg_lst.py 20230101 20231231 data/raw/lst data/processed/lst

# Concat inmet data
#python src/unify_inmet.py data/raw/lst data/raw/inmet data/processed/inmet --aggregated

# Build
#python src/build_dataset.py