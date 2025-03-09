import streamlit as st

st.set_page_config(page_title="Welcome | Pollen Allergy Forecast", page_icon="🌿")

st.title("🌍 Welcome to the Pollen Allergy Forecast")
st.subheader("Helping you manage pollen exposure and stay healthy.")

st.write(
    """
    If you suffer from pollen allergies, staying informed about pollen levels can make a big difference.  
    This project aims to help individuals anticipate high pollen days and take necessary precautions,  
    such as staying indoors or taking antihistamine medication when needed.
    """
)

st.write(
    """
    ### Data Source  
    All pollen forecast data is provided by **Copernicus Atmosphere Monitoring Service (CAMS)**,  
    """
)

st.write(
    """
    ---
    *This is a personal project by [Lucas Scellos](https://lucasscellos.github.io), built during my free time.  
    Feel free to check out my other projects and get in touch!*  
    """
)
