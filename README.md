# 🌍 Real-Time AQI Dashboard

A clean and simple web app built with **Streamlit** that displays real-time Air Quality Index (AQI) data from anywhere in the world using the **IQAir AirVisual API**.

---

## 🚀 Live Demo

[Click here to open the app](https://rupal0912-real-time-aqi-app-ntbf1g.streamlit.app/)

---

## 📌 Features

- 🔎 Search by City, State, and Country  
- 📊 Real-time AQI (US Standard)  
- 🌡️ Temperature, Humidity, and Wind Speed  
- 🔍 Displays the primary pollutant  
- 🎨 Deployed on Streamlit Cloud for easy access  

---

## 🛠️ Tech Stack

- **Frontend & UI:** Streamlit  
- **API:** IQAir AirVisual API  
- **Language:** Python  
- **Hosting:** Streamlit Cloud  

---

## 🔧 Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/Rupal0912/real_time_aqi.git
    cd real_time_aqi
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the app locally:

    ```bash
    streamlit run app.py
    ```

---

## 🔐 API Key Setup

To get AQI data, you need an API key from [IQAir AirVisual](https://www.iqair.com/air-pollution-data-api).

- Sign up and get your API key.
- For local development, create a `.streamlit/secrets.toml` file with the following content:

    ```toml
    AIR_QUALITY_API_KEY = "your_api_key_here"
    ```

- Your app reads the API key securely from this file.

---

## 📄 License

MIT License © [Rupal Tripathi]

---

## 🙌 Contributions

Feel free to open issues or submit pull requests!
