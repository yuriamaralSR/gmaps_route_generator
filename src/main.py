from read_spreadsheet import FILE_PATH, read_spreadsheet, group_packs_by_address
from generate_kml import generate_kml

def main():
    try:
        print("[INFO] Reading the spreadsheet...")
        df = read_spreadsheet(FILE_PATH)

        if df is None:
            print("[ERRO] Failed to read spreadsheet!")
            return

        print("[INFO] Grouping packs...")
        grouped_df = group_packs_by_address(df)

        print("[INFO] Generating the KML file...")
        kml = generate_kml(grouped_df)

        if kml:
            print("[SUCCESS] KML file generated successfully!")
        else:
            print("[ERROR] Failed to generate KML file")

    except Exception as e:
        print(f"[FATAL] Unexpected error: {e}")

if __name__ == "__main__":
    main()