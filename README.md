# Cafe Sales Data Cleaning & Analysis

A Python script (`Pandas.py`) that loads a messy cafe sales dataset, cleans it up, and performs basic exploratory analysis and visualization using `pandas`, `matplotlib`, and `seaborn`.

## Contents

| File | Description |
|---|---|
| `Pandas.py` | Main script: loads, cleans, analyzes, visualizes, and merges the cafe sales dataset. |
| `dirty_cafe_sales.csv` | Raw input dataset containing cafe transaction records with intentional data quality issues. |

## Requirements

- Python 3.x
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)

Install dependencies:

```bash
pip install pandas matplotlib seaborn
```

## Dataset

`dirty_cafe_sales.csv` contains transaction-level cafe sales data with the following columns:

| Column | Description |
|---|---|
| `Transaction ID` | Unique identifier for each transaction |
| `Item` | Item purchased (e.g., Coffee, Cake, Sandwich) |
| `Quantity` | Number of items purchased |
| `Price Per Unit` | Price per item |
| `Total Spent` | Total amount spent on the transaction |
| `Payment Method` | Cash, Credit Card, or Digital Wallet |
| `Location` | In-store or Takeaway |
| `Transaction Date` | Date of the transaction |

The dataset intentionally includes messy values such as `ERROR`, `UNKNOWN`, and blank entries to simulate real-world dirty data.

## What the Script Does

1. **Loads** the CSV file into a pandas DataFrame and prints summary info (`.info()`).
2. **Diagnoses data quality issues**: counts duplicate rows and missing values per column.
3. **Cleans column names** by stripping whitespace.
4. **Fixes data types**:
   - Converts `Quantity`, `Price Per Unit`, and `Total Spent` to numeric (invalid values like `ERROR`/`UNKNOWN` become `NaN`).
   - Converts `Transaction Date` to datetime.
5. **Removes rare/noisy labels**: for categorical (string) columns, replaces values that occur in less than 6% of rows with missing (`pd.NA`), except for `Transaction ID`.
6. **Imputes missing values**:
   - Categorical columns (`Item`, `Payment Method`, `Location`) are filled with their most frequent value (mode).
   - Numeric columns (`Price Per Unit`, `Total Spent`, `Quantity`) are filled with their mean.
   - `Transaction Date` is filled with the mean date.
7. **Drops** the `Transaction ID` column (not needed for analysis/training).
8. **Prints summary statistics**: dataset shape, head, `.describe()`, and value counts for `Item`, `Payment Method`, and `Location`.
9. **Visualizes the data**:
   - A histogram (with KDE) of `Total Spent`.
   - A pie chart showing the distribution of `Location` (In-store vs. Takeaway).
10. **Merges datasets**: reloads the original CSV and performs an inner join with the cleaned DataFrame on the `Item` column, then prints the merged result's head, shape, and info.

## Usage

Make sure `dirty_cafe_sales.csv` is in the same directory as the script, then run:

```bash
python Pandas.py
```

The script will print cleaning diagnostics and statistics to the console, and display two plots (a histogram and a pie chart) in separate windows.

## Notes

- The script uses colored terminal output (ANSI escape codes) to highlight warnings, errors, and key results.
- The "rare label removal" step (values under 6% frequency replaced with `NaN`) is a simplistic noise-reduction technique — it may also remove legitimate but uncommon values, so use with care on other datasets.
- The merge step joins the dataset with itself (`dirty_cafe_sales.csv` loaded twice) on `Item`, which is mainly meant to demonstrate `pd.merge` usage rather than to produce new analytical insight.
