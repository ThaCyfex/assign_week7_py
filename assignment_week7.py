# Importing the necessary libraries for data manipulation and visualization.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Handling potential errors that might occur while reading the dataset file.
try:
    # Loading the dataset. The file path 'dataset.csv' should be replaced with the actual dataset path.
    df = pd.read_csv('dataset.csv')
except FileNotFoundError:
    # If the file is not found, I print an error message and exit the script.
    print("Error: The file was not found. Please check the file path.")
    exit()

# Defining the column names that I will be working with. These should match the dataset's column names.
CATEGORY_COLUMN = 'category_column'
NUMERICAL_COLUMN = 'numerical_column'
NUMERICAL_COLUMN_1 = 'numerical_column_1'
NUMERICAL_COLUMN_2 = 'numerical_column_2'
TIME_COLUMN = 'time_column'
VALUE_COLUMN = 'value_column'

# Task 1: Loading and exploring the dataset.
print("\nTask 1: Load and Explore the Dataset")

# Displaying the first few rows of the dataset to get an initial look at the data.
print("\nFirst few rows of the dataset:")
print(df.head(10))  # Showing 10 rows instead of the default 5 for a better overview.

# Exploring the structure of the dataset to understand its columns, data types, and non-null counts.
print("\nDataset Information:")
print(df.info())

# Checking for any missing values in the dataset to identify potential data quality issues.
print("\nMissing Values Count:")
print(df.isnull().sum())

# Cleaning the dataset by forward-filling missing values to ensure no gaps in the data.
print("\nCleaning the dataset...")
df.fillna(method='ffill', inplace=True)  # Using forward fill to handle missing values.
print("Missing values handled.")

# Task 2: Performing basic data analysis.
print("\nTask 2: Basic Data Analysis")

# Computing basic statistics for numerical columns to summarize the data distribution.
print("\nBasic Statistics of Numerical Columns:")
print(df.describe())

# Grouping the data by a categorical column and calculating the mean of a numerical column for each group.
if CATEGORY_COLUMN in df.columns and NUMERICAL_COLUMN in df.columns:
    grouped = df.groupby(CATEGORY_COLUMN)[NUMERICAL_COLUMN].mean()
    print("\nGroup-wise Mean:")
    print(grouped)
else:
    # If the required columns are missing, I print a warning and skip this step.
    print(f"Warning: Columns '{CATEGORY_COLUMN}' or '{NUMERICAL_COLUMN}' are missing. Skipping group-wise mean calculation.")

# Task 3: Creating visualizations to better understand the data.
print("\nTask 3: Data Visualization")

# Creating a line chart to show trends over time using the time and value columns.
if TIME_COLUMN in df.columns and VALUE_COLUMN in df.columns:
    plt.figure(figsize=(10, 6))
    plt.plot(df[TIME_COLUMN], df[VALUE_COLUMN], color='blue')
    plt.title('Trends Over Time')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
else:
    # If the required columns are missing, I print a warning and skip the line chart.
    print(f"Warning: Columns '{TIME_COLUMN}' or '{VALUE_COLUMN}' are missing. Skipping line chart.")

# Creating a bar chart to compare the average of a numerical column across categories.
if CATEGORY_COLUMN in df.columns and NUMERICAL_COLUMN in df.columns:
    plt.figure(figsize=(10, 6))
    df.groupby(CATEGORY_COLUMN)[NUMERICAL_COLUMN].mean().plot(kind='bar', color='orange', edgecolor='black')
    plt.title('Comparison Across Categories')
    plt.xlabel('Category')
    plt.ylabel('Average Value')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
else:
    # If the required columns are missing, I print a warning and skip the bar chart.
    print(f"Warning: Columns '{CATEGORY_COLUMN}' or '{NUMERICAL_COLUMN}' are missing. Skipping bar chart.")

# Creating a histogram to show the distribution of a numerical column.
if NUMERICAL_COLUMN in df.columns:
    plt.figure(figsize=(10, 6))
    plt.hist(df[NUMERICAL_COLUMN], bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribution of Numerical Column')
    plt.xlabel('Numerical Column')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
else:
    # If the required column is missing, I print a warning and skip the histogram.
    print(f"Warning: Column '{NUMERICAL_COLUMN}' is missing. Skipping histogram.")

# Creating a scatter plot to visualize the relationship between two numerical columns.
if NUMERICAL_COLUMN_1 in df.columns and NUMERICAL_COLUMN_2 in df.columns:
    plt.figure(figsize=(10, 6))
    plt.scatter(df[NUMERICAL_COLUMN_1], df[NUMERICAL_COLUMN_2], c='green', alpha=0.7)
    plt.title('Relationship Between Two Numerical Columns')
    plt.xlabel('Numerical Column 1')
    plt.ylabel('Numerical Column 2')
    plt.grid(alpha=0.5)
    plt.show()
else:
    # If the required columns are missing, I print a warning and skip the scatter plot.
    print(f"Warning: Columns '{NUMERICAL_COLUMN_1}' or '{NUMERICAL_COLUMN_2}' are missing. Skipping scatter plot.")

# Indicating that the script has completed successfully.
print("\nScript Execution Completed Successfully!")
