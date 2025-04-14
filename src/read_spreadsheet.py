import pandas as pd
import re
import glob 

def get_file():
    list_of_files = glob.glob('data/*.xlsx')
    if not list_of_files:
        print("No Excel files found in the 'data' directory.")
        return None
    
    if len(list_of_files) == 1:
        file_path = list_of_files[0]
        return file_path
    
    print("Multiple Excel files found. Choose one: ")
    for index, file in enumerate(list_of_files):
        print(f"{index + 1}: {file}")
    
    choice = int(input("Enter the number of the file: ")) - 1
    return list_of_files[choice] if 0 <= choice < len(list_of_files) else None

FILE_PATH = get_file()

def read_spreadsheet(file_path):
    if file_path is None:
        return None
    try:
        df = pd.read_excel(file_path)
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError as e:
        print(f"Error reading the Excel file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def count_packs(df):
    df = df.copy()
    df['Number of Packs'] = df['Sequence'].astype(str).apply(lambda x: len(re.findall(r'\d+', x)))
    return df

def group_packs_by_address(df):
    df_subset = df.loc[:, ['Sequence', 'Destination Address', 'Neighborhood', 'Latitude', 'Longitude']].copy()
    df_subset['Sequence'] = df_subset['Sequence'].astype(str)
    fixing_lat_long_format(df_subset)
    
    grouped = df_subset.groupby(['Latitude', 'Longitude'], as_index=False).agg({
        'Sequence': lambda x: ', '.join(x),
        'Neighborhood' : 'first',
        'Destination Address': 'first'
        })
    count_packs(grouped)    
    
    return grouped

def fixing_lat_long_format(df):
    df[['Latitude', 'Longitude']] /= 10_000_000
    return df