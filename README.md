# AgriculturalDataCleaner


## Overview
The **AgriculturalDataCleaner** is a Python script designed to clean and preprocess agricultural datasets. It ensures that data is properly formatted, standardized, and ready for analysis by performing operations such as removing duplicates, handling missing values, and normalizing crop names.

This script is particularly useful for research and data analysis projects, including those related to **Living Stones Foundation**, where agricultural data is analyzed to understand trends, optimize resource allocation, and support decision-making in farming and food production.

## Features
1. **Loads data** from both `.xlsx` and `.csv` files.
2. **Cleans the data** by:
   - Removing duplicate rows.
   - Dropping columns and rows with excessive missing values.
   - Replacing inconsistent values with standardized names.
3. **Normalizes crop names** (e.g., converting "Crop A - Wheat" to "Wheat").
4. **Converts cleaned datasets** into `.csv` format.
5. **Stores the cleaned files** in the `cleaned_data` directory.

## Prerequisites
- Python 3.x
- Required libraries:
  ```bash
  pip install pandas openpyxl
  ```

## Usage
1. Place all `.xlsx` and `.csv` agricultural data files in the same directory as the script.
2. Run the script using:
   ```bash
   python main.py
   ```
3. The cleaned datasets will be saved in the `cleaned_data` folder.

## Contribution to Living Stones Foundation
The **Living Stones Foundation** focuses on data-driven decision-making, including **big data analytics for agricultural trends and donor contributions**. This script plays a crucial role by:
1. **Ensuring data accuracy** for predictive models in farming and food production.
2. **Standardizing agricultural datasets** to support effective fundraising and resource allocation.
3. **Providing structured and clean data** for in-depth analysis using SQL, Python, and Power BI.

## Issues & Future Enhancements
- Improve handling of additional agricultural data inconsistencies.
- Expand crop name normalization for more extensive datasets.
- Integrate machine learning techniques for automated data validation.

## Author
**Taemoor Hasan**

