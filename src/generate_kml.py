from simplekml import Kml

def generate_kml(df):
    if df is not None:
        kml = Kml()
        for index, row in df.iterrows():
            point = kml.newpoint(name=f"{row['Sequence']} - {(row['Destination Address'])}", coords=[(row['Longitude'], row['Latitude'])])
            point.description = f"Nº Packs: {(row['Number of Packs'])}"
        
        kml.save("output.kml")
        return kml
    else:
        print("No data to generate KML.")
        return None