# CSV Data Cleaner

This is a Python script that cleans data in a CSV file. It removes duplicates, empty columns, inconsistent values, duplicated columns, and columns that contain the same value for all lines. It also removes values that are specified as `None` values. The cleaned data is saved to a new CSV file.

## Usage

1. Clone this repository:

    ```
    git clone https://github.com/btt1996/csv_data_cleaner.git
    ```

2. Install the required packages:

    ```
    pip install pandas tqdm
    ```

3. Put your input CSV file in the `data` directory.

4. Open `main.py` and modify the input parameters as needed:

    ```python
    file_path = 'data/your_file.csv'
    none_values = ['none', 'unfound', 'unknown']
    allowed_values = {'column1': ['value1', 'value2'], 'column2': ['value3', 'value4']}
    ```

5. Run the script:

    ```
    python main.py
    ```

6. The cleaned data will be saved to a new CSV file named `cleaned_data.csv` in the `data` directory.

## License

This project is licensed under the MIT License. Feel free to use and modify this script as needed.

## Author

This script was created by btt1996 (https://github.com/Btt1996).
