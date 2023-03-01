import pandas as pd
import matplotlib.pyplot as plt


def analyze_data(file_path):
    """Analyzes the data in the input CSV file"""
    data = pd.read_csv(file_path)

    # Count the number of rows and columns in the data
    num_rows, num_cols = data.shape
    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_cols}")

    # Count the number of unique values in each column
    unique_values = data.nunique()
    print("Number of unique values in each column:")
    print(unique_values)

    # Plot a histogram of the number of missing values in each row
    num_missing_values = data.isna().sum(axis=1)
    plt.hist(num_missing_values, bins=50)
    plt.title("Number of missing values in each row")
    plt.xlabel("Number of missing values")
    plt.ylabel("Number of rows")
    plt.show()


if __name__ == '__main__':
    # Analyze the input data
    print("Analyzing the input data...")
    analyze_data('data/data.csv')

    # Analyze the cleaned data
    print("Analyzing the cleaned data...")
    analyze_data('data/cleaned_data.csv')
