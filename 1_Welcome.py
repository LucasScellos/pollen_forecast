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
    All pollen forecast data is provided by **Copernicus Atmosphere Monitoring Service (CAMS)**,  precision is about 11km and refresh every day.
    """
)

st.write(
    """
    ---
    ### 💡 Why I Created This Project  
    I, along with my family and friends, suffer from pollen allergies, making it incredibly difficult to track 
    and anticipate high pollen days. The available tools were either inaccurate or lacked real-time forecasting, 
    making allergy management a challenge. This project was built to **help people like us prepare for allergy season**, 
    especially as **spring approaches**, so we can take precautions in advance.
    
    *This is a personal project by [Lucas Scellos](https://lucasscellos.github.io), built during a week-end.  
    Feel free to check out my other projects and get in touch!*  
    """
)