'''
AgriculturalDataCleaner

Main.py

designed to clean and preprocess agricultural datasets

1. Loads data from both .xlsx and .csv  files.

2. Cleans the data by removing duplicate rows and dropping rows with excessive missing values.

3. Normalizes inconsistent crop names (such as "Crop A - Wheat" to "Wheat").

4. Converts all cleaned datasets to CSV format.

5. Saves the cleaned files in a "cleaned_data" folder.

Author: Taemoor Hasan
'''

import pandas as pd
import os

# need to download pip install openpyxl

# folder for cleaned files
cleaned_dir = "cleaned_data"
os.makedirs(cleaned_dir, exist_ok=True)

# File paths
files = [
    "Ag Trends in South America (2013-2023).xlsx",
    "Agricultural Trends in South America.xlsx",
    "FAOSTAT_data_en_2-24-2025.csv",
    "Argentina_Sheep_Farming_CNA18_C_5_6.xlsx"
]


# to clean dataset
def clean_dataset(df, crop_column=None):

    # replace - with NONE, but keep 's'
    df.replace(["-", ""], pd.NA, inplace=True)

    # removes duplicate rows
    df = df.drop_duplicates()

    #remove columns where the majority of empty values exist
    df = df.dropna(axis=1, thresh=len(df) * 0.5)

    #remove rows where the majority of empty values exist
    df = df.dropna(axis=0, thresh=len(df.columns) * 0.5)

    if crop_column and crop_column in df.columns:
        standardization_map = {
            "Crop A - Wheat": "Wheat",
            "Whet": "Wheat",
            "Maiz": "Corn",
            "Zea Mays": "Corn",
            "Soyabeans": "Soybeans"
        }
        df[crop_column] = df[crop_column].replace(standardization_map)

    return df


# Process each file
for file in files:

    # skipping missing files (safety)
    if not os.path.exists(file):
        print(f"File not found: {file}")
        continue

        # Load data and reading it
    if file.endswith(".xlsx"):
        xls = pd.ExcelFile(file)

        for sheet_name in xls.sheet_names:
            df = xls.parse(sheet_name)
            cleaned_df = clean_dataset(df)

            if not cleaned_df.empty:
                csv_file_path = os.path.join(cleaned_dir, f"cleaned_{sheet_name}.csv")
                cleaned_df.to_csv(csv_file_path, index=False)
                print(f"Cleaned data from sheet {sheet_name} saved as {csv_file_path}")
            else:
                print(f"Skipping empty cleaned dataset for sheet {sheet_name}")

    elif file.endswith(".csv"):
        df = pd.read_csv(file)
        cleaned_df = clean_dataset(df)
        
        if not cleaned_df.empty:
            output_file = os.path.join(cleaned_dir, "cleaned_" + os.path.splitext(file)[0] + ".csv")
            cleaned_df.to_csv(output_file, index=False)
            print(f"Cleaned data saved as {output_file}")
        else:
            print(f"Skipping empty cleaned dataset for {file}")

# By Taemoor Hasan
