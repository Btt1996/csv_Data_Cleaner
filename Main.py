from data_cleaning import clean_data
from tqdm import tqdm


if __name__ == '__main__':
    # Define input parameters
    file_path = 'data.csv'
    none_values = ['none', 'unfound', 'unknown']
    allowed_values = {'column1': ['value1', 'value2'], 'column2': ['value3', 'value4']}

    # Clean the data
    print("Cleaning the data...")
    cleaned_data = clean_data(file_path, none_values, allowed_values)

    # Save the cleaned data to a new CSV file
    print("Saving the cleaned data...")
    cleaned_data.to_csv('cleaned_data.csv', index=False)

    # Add a progress bar for each task running
    for i in tqdm(range(10)):
        pass  # Do some dummy task to demonstrate the progress bar
