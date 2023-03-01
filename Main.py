import os
import subprocess

# Define a list of available scripts and their corresponding filenames
scripts = [
    {"name": "Clean CSV data", "filename": "clean_csv.py"},
    {"name": "Before-cleaning analysis", "filename": "before_cleaning_analysis.py"},
    {"name": "After-cleaning analysis", "filename": "after_cleaning_analysis.py"},
    {"name": "Plot statistics", "filename": "plot_statistics.py"},
    {"name": "Convert to database format", "filename": "convert_to_db.py"},
    # Add more scripts here as needed
]

# Display the available scripts and prompt the user to choose one
print("Available scripts:")
for i, script in enumerate(scripts):
    print(f"{i+1}. {script['name']}")
choice = input("Enter the number of the script you want to run: ")
try:
    choice = int(choice)
    if choice < 1 or choice > len(scripts):
        raise ValueError
except ValueError:
    print("Invalid choice. Please enter a number between 1 and", len(scripts))
    exit()

# Run the selected script
script_name = scripts[choice-1]["name"]
script_filename = scripts[choice-1]["filename"]
print(f"\nRunning script: {script_name}\n")
subprocess.run(["python", script_filename])

# Wait for user to press Enter before exiting
input("\nPress Enter to exit...")
