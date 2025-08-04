import os
import pandas as pd # pyright: ignore[reportMissingModuleSource]

df = pd.read_csv(r"D:\Bedo project\student_dataset.csv") # Read CSV file
df.drop(columns=["Phone_No.", "Roll No.", "School Name", "Student Address"], inplace=True) # Drop unneeded columns (data cleaning)
print(df.columns)
print(df.head())
#print(df.info()) # Show DataFrame structure
#print(df.describe()) # Show summary statistics
