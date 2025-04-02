import pandas as pd
import glob 

def get_file():
    list_of_files = glob.glob('data/*.xlsx')
    if not list_of_files:
        print("No Excel files found in the 'data' directory.")
        return None
    
    file_path = list_of_files[0]
    return file_path

FILE_PATH = get_file()

def read_spreasheet(file_path):
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

def group_packs_by_address(df):
    df_subset = df.loc[:, ['Sequence', 'Destination Address', 'Latitude', 'Longitude']].copy()
    df_subset['Sequence'] = df_subset['Sequence'].astype(str)
    
    grouped = df_subset.groupby(['Latitude', 'Longitude'], as_index=False).agg({
        'Sequence': lambda x: ', '.join(x),
        'Destination Address': 'first'
    })
    return grouped

if __name__ == "__main__":
    df = read_spreasheet(FILE_PATH)
    if df is not None:
        grouped_df = group_packs_by_address(df)
        print(grouped_df)
