import streamlit as st
import logging
import os
from datetime import date
from utils import front
from scripts import download_data_day_france as dd

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Streamlit Page Configuration
st.set_page_config(page_title="Pollen Allergy Forecast", page_icon="🌿")

st.title("🌿 Pollen Allergy Forecast")
st.subheader("Stay informed about pollen levels and protect yourself from allergies.")

# Dataset path
DATASET_PATH = "data/raw_data/copernicus/ENS_FORECAST.nc"


def ensure_dataset():
    """Check if dataset exists, if not, download it."""
    if not os.path.exists(DATASET_PATH):
        logging.warning("Dataset file not found! Downloading new data...")
        #st.warning("⚠️ Data file is missing! Downloading new data...")
        with st.status("Downloading new forecast from Copernicus, please wait...", expanded=True) as status:
            dd.retrieve_data()
            status.update(label="✅ Download complete!", state="complete", expanded=False)
        #st.success("New data has been successfully downloaded. Please refresh the page.")


def main():
    """Main function to handle user input and display pollen forecasts."""
    ensure_dataset()

    # User input: Address
    address = st.text_input("📍 Enter your location in France:", value="Paris Rue de Rocroy")

    if address:
        try:
            lat, lon, city_name = front.get_coordinates(address)
            logging.info(f"User location resolved: {city_name} (Lat: {lat}, Lon: {lon})")

            # Load and process data
            dataset = front.load_dataset(DATASET_PATH)
            df_hours, df_days, formatted_date = front.load_preprocess(dataset, lat, lon)

            # Display pollen concentration charts
            st.plotly_chart(front.plot_pollen_concentration_hours(df_hours, formatted_date, city_name))
            st.plotly_chart(front.plot_pollen_concentration_days(df_days, formatted_date, city_name))

            # Ensure data freshness
            today = date.today()
            if formatted_date != f"{today.year}, {today.strftime('%B')}, {today.day}":
                st.warning("⚠️ Data is outdated! Downloading new data...")
                with st.status("Downloading new data, please wait...", expanded=True) as status:
                    logging.info("Data outdated, fetching latest data...")
                    dd.retrieve_data()
                    status.update(label="✅ Download complete!", state="complete", expanded=False)
                st.success("New data has been successfully downloaded. Please refresh the page.")

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
            logging.error(f"Error processing location: {e}")


if __name__ == "__main__":
    main()
