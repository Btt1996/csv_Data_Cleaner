import pandas as pd
from utils import *


def clean_data(file_path: str, none_values: list, allowed_values: list) -> pd.DataFrame:
    """Clean data in a given CSV file."""
    df = pd.read_csv(file_path)

    # Remove duplicates
    print("Removing duplicates...")
    df = remove_duplicates(df)

    # Remove empty columns
    print("Removing empty columns...")
    df = remove_empty_columns(df)

    # Remove inconsistent values
    print("Removing inconsistent values...")
    for column in allowed_values:
        df = remove_inconsistent_values(df, column, allowed_values[column])

    # Remove duplicated columns
    print("Removing duplicated columns...")
    df = remove_duplicated_columns(df)

    # Remove columns with same value for all lines
    print("Removing columns with same value for all lines...")
    df = remove_same_value_columns(df)

    # Remove None values
    print("Removing None values...")
    df = remove_none_values(df, none_values)

    return df
