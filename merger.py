import pandas as pd
import os

# Set the path to the directory containing the CSV files
folder_path = "/Users/rishabhbhartiya/Desktop/BHAGWAD GEETA/chapter"

# List of filenames in the desired order
file_order = [
    "Bhagvad Chapter 1.csv",
    "Bhagvad Chapter 2.csv",
    "Bhagvad Chapter 3.csv",
    "Bhagvad Chapter 4.csv",
    "Bhagvad Chapter 5.csv",
    "Bhagvad Chapter 6.csv",
    "Bhagvad Chapter 7.csv",
    "Bhagvad Chapter 8.csv",
    "Bhagvad Chapter 9.csv",
    "Bhagvad Chapter 10.csv",
    "Bhagvad Chapter 11.csv",
    "Bhagvad Chapter 12.csv",
    "Bhagvad Chapter 13.csv",
    "Bhagvad Chapter 14.csv",
    "Bhagvad Chapter 15.csv",
    "Bhagvad Chapter 16.csv",
    "Bhagvad Chapter 17.csv",
    "Bhagvad Chapter 18.csv",
]

# Create an empty list to hold the DataFrames
dataframes = []

# Loop through the filenames in the specified order
for file in file_order:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv("Final_File.csv", index=False)
