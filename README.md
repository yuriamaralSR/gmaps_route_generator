## 📦  Project Name
GMaps Route Generator

---

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Release](https://img.shields.io/badge/Version-1.0.0-informational?style=flat-square)


## 📝 Description   
This project aims to read a delivery spreadsheet (manifest) and generate a `.kml` file compatible with the Google Maps for route visualization.

---

## 🧰 Features
- Reads `.xlsx` delivery spreadsheets;
- Group packages by address;
- Automatically corrects latitude and longitude format;
- Generates a `KML` file for visualization on Google Maps;
- Count packages per delivery location.

---

## 📂 Project Structure
```
/
├── data/                      # Input spreadsheets (.xlsx)
├── src/
│   ├── read_spreadsheet.py   # Module for reading and processing spreadsheets
│   ├── generate_kml.py       # Module for KML generation
│   └── main.py               # Main executable script
├── output.kml                # Generated KML file (example)
├── README.md                 # Docs
```

---

## 📋 Requirements
```
Python 3.9+
pandas
openpyxl
simplekml
```

---

## 🚀 How to Run
```bash
# 1. Clone the repository
git clone https://github.com/yuriamaralSR/gmaps_route_generator

# 2. Make sure your virtual environment is activated
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate.bat    # Windows

# 3. Install the dependencies
pip install -r requirements.txt

# 4. PLace a file .xlsx in the /data directory
# 5. Run the main script
python src/main.py
```

---

## 📤 Example Output
```bash
[INFO] Reading the spreadsheet data\your-spreadsheet.xlsx...
[INFO] Grouping packs...
[INFO] Generating the KML file...
[SUCCESS] KML file generated successfully!
```

---

## ✅ Spreadsheet Format
The spreadsheet must contain at last the following columns:
- Sequence
- Destination Address
- Latitude
- Longitude

---

## 💡 Notes
- Coordinates are automatically adjusted from integer to float format (e.g., 228000000 -> 22.8000000);
- The generated `output.kml` file will be saved in the project root directory.
- Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 👥 Contributors

<table>
  <tr>
    <td align="center"><a href="https://github.com/yuriamaralSR"><img src="https://avatars.githubusercontent.com/yuriamaralSR" width="100px;" alt=""/><br /><sub><b>Yuri Amaral</b></sub></a><br />💻 📝 🚀</td>
  </tr>
</table>