import cdsapi
import zipfile
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants
URL = "https://ads.atmosphere.copernicus.eu/api"
CDS_API_KEY = os.getenv("CDS_API_KEY")
DATASET = "cams-europe-air-quality-forecasts"
SAVE_PATH = "data/raw_data/copernicus/test.zip"

# Area coordinates for France
FRENCH_AREA = [51.05, -4.47, 42.20, 8.13]


def get_today_date():
    """Returns today's date in the format: ['YYYY-MM-DD/YYYY-MM-DD']"""
    today = datetime.today().strftime("%Y-%m-%d")
    return [f"{today}/{today}"]


def unzip_file(zip_path):
    """Unzips the file to its containing directory."""
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(os.path.dirname(zip_path))
        logging.info(f"Successfully extracted: {zip_path}")
    except Exception as e:
        logging.error(f"Failed to unzip {zip_path}: {e}")
        raise


def retrieve_data():
    """Retrieves data from the Copernicus API and extracts it."""
    if not CDS_API_KEY:
        logging.error("CDS_API_KEY is not set. Please add it to your environment variables.")
        return

    client = cdsapi.Client(url=URL, key=CDS_API_KEY)
    
    request_params = {
        "variable": ["alder_pollen", "birch_pollen", "grass_pollen", "mugwort_pollen", "olive_pollen"],
        "model": ["ensemble"],
        "level": ["0"],
        "date": get_today_date(),
        "type": ["forecast"],
        "time": ["00:00"],
        "leadtime_hour": ["0", "2", "4", "6", "8", "10", "12", "16", "18", "20", "22", "24", "48", "72", "96"],
        "data_format": "netcdf_zip",
        "area": FRENCH_AREA
    }

    try:
        logging.info("Requesting data from Copernicus API...")
        client.retrieve(DATASET, request_params).download(SAVE_PATH)
        logging.info(f"Data downloaded successfully: {SAVE_PATH}")
        
        unzip_file(SAVE_PATH)

    except Exception as e:
        logging.error(f"Data retrieval failed: {e}")
        raise


if __name__ == "__main__":
    retrieve_data()
