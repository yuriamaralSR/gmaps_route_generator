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
