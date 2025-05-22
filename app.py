
import streamlit as st
import requests
import os
import matplotlib.pyplot as plt

st.title("🌍 Real-Time AQI Dashboard")

# Get API key from environment variable or fallback to your hardcoded key
API_KEY = API_KEY = st.secrets["AIR_QUALITY_API_KEY"]

city = st.text_input("Enter City", value="Delhi")
state = st.text_input("Enter State", value="Delhi")
country = st.text_input("Enter Country", value="India")

def get_aqi_data(city, state, country):
    url = f"http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if st.button("Get AQI"):
    if not city.strip() or not state.strip() or not country.strip():
        st.warning("Please enter City, State, and Country.")
    else:
        with st.spinner("Fetching air quality data..."):
            data = get_aqi_data(city, state, country)
        if data and data.get("status") == "success":
            pollution = data["data"]["current"]["pollution"]
            weather = data["data"]["current"]["weather"]

            st.subheader(f"📍 {city}, {state}, {country}")
            st.metric(label="AQI (US)", value=pollution["aqius"])
            st.write(f"Main Pollutant: {pollution['mainus'].upper()}")
            st.write(f"Temperature: {weather['tp']}°C")
            st.write(f"Humidity: {weather['hu']}%")
            st.write(f"Wind Speed: {weather['ws']} m/s")

            # Weather bar chart
            labels = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)']
            values = [weather['tp'], weather['hu'], weather['ws']]

            fig, ax = plt.subplots()
            ax.bar(labels, values, color=['#ff6347', '#1e90ff', '#3cb371'])
            ax.set_ylim(0, max(values) + 10)
            st.pyplot(fig)

        else:
            st.error("Could not fetch AQI data. Check city/state/country names or API key.")
