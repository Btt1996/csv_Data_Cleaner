import pandas as pd
from tqdm import tqdm


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicates from a DataFrame."""
    df.drop_duplicates(inplace=True)
    return df


def remove_empty_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Remove empty columns from a DataFrame."""
    df.dropna(axis=1, how='all', inplace=True)
    return df


def remove_inconsistent_values(df: pd.DataFrame, column: str, allowed_values: list) -> pd.DataFrame:
    """Remove inconsistent values from a DataFrame."""
    df = df[~df[column].isin(allowed_values)]
    return df


def remove_duplicated_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicated columns from a DataFrame."""
    df = df.loc[:, ~df.columns.duplicated()]
    return df


def remove_same_value_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Remove columns that contain the same value for all lines."""
    for column in tqdm(df.columns):
        if len(df[column].unique()) == 1:
            df.drop(column, axis=1, inplace=True)
    return df


def remove_none_values(df: pd.DataFrame, none_values: list) -> pd.DataFrame:
    """Remove None values from a DataFrame."""
    for value in none_values:
        df.replace(value, pd.NA, inplace=True)
    return df
