from simplekml import Kml
from read_spreadsheet import *

def generate_kml(df):
    if df is not None:
        kml = Kml()
        for index, row in df.iterrows():
            point = kml.newpoint(name=f"Point {index} -- {(row['Destination Address'])}", coords=[(row['Longitude'], row['Latitude'])])
            point.description = f"Ordem: {(row['Sequence'])}"
        
        kml.save("output.kml")
        return kml
    else:
        print("No data to generate KML.")
        return None

if __name__ == "__main__":
    df = read_spreasheet(FILE_PATH)
    if df is not None:
        grouped_df = group_packs_by_address(df)
        kml = generate_kml(grouped_df)
        print(kml.kml())