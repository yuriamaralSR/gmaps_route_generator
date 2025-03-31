import pandas as pd
import glob 

def get_file():
    list_of_files = glob.glob('data/*.xlsx')
    file_path = list_of_files[0]
    return file_path

FILE_PATH = get_file()

def read_spreasheet(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    return None

def group_packs_by_address(df):
    df_subset = df.loc[:, ['Sequence', 'Latitude', 'Longitude']]
    df_subset['Sequence'] = df_subset['Sequence'].astype(str)
    
    grouped = df_subset.groupby(['Latitude', 'Longitude'], as_index=False).agg({
        'Sequence': lambda x: ', '.join(x)
    })
    return grouped

if __name__ == "__main__":
    df = read_spreasheet(FILE_PATH)
    if df is not None:
        grouped_df = group_packs_by_address(df)
        print(grouped_df)
