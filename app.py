import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Sales Forecast", layout="centered")

# Title
st.title("Sales Forecast Prediction App")
st.markdown("Predict future sales based on business inputs")

# Sidebar
st.sidebar.header("⚙️ Business Scenario")
scenario = st.sidebar.selectbox(
    "Select Budget Scenario",
    ["Low Budget", "Medium Budget", "High Budget"]
)

# Default values based on scenario
if scenario == "Low Budget":
    adv_default, trend_default, pipeline_default = 1000, 30, 40
elif scenario == "Medium Budget":
    adv_default, trend_default, pipeline_default = 5000, 60, 60
else:
    adv_default, trend_default, pipeline_default = 10000, 80, 80

# Input section
st.markdown("### Enter Business Inputs")

advertising = st.slider("Advertising Spend (₹)", 0, 20000, adv_default)
trend = st.slider("Market Trend Index (0–100)", 0, 100, trend_default)
pipeline = st.slider("Sales Pipeline Strength (%)", 0, 100, pipeline_default)

region = st.selectbox("Region", ["North", "South", "East", "West"])
season = st.selectbox("Season", ["Q1", "Q2", "Q3", "Q4"])

# Encode categorical variables
region_encoded = ["North", "South", "East", "West"].index(region)
season_encoded = ["Q1", "Q2", "Q3", "Q4"].index(season)

# Load model
try:
    model = joblib.load("best_model.pkl")
    st.success("Model loaded successfully")
except:
    st.error("❌ Model not found. Please upload best_model.pkl")
    model = None

# Prediction
if st.button("Predict Sales 🚀"):
    if model:
        input_data = np.array([[advertising, trend, pipeline, region_encoded, season_encoded]])
        prediction = model.predict(input_data)[0]

        # Display result
        st.markdown("### 📈 Prediction Result")
        st.success(f"💰 Predicted Sales: ₹ {prediction:,.2f}")

        # Visualization
        st.markdown("### 📊 Visualization")

        data = pd.DataFrame({
            "Category": ["Advertising", "Market Trend", "Pipeline Strength", "Predicted Sales"],
            "Value": [advertising, trend, pipeline, prediction]
        })

        fig, ax = plt.subplots()
        ax.bar(data["Category"], data["Value"])
        ax.set_xlabel("Factors")
        ax.set_ylabel("Value")
        ax.set_title("Business Inputs vs Predicted Sales")

        st.pyplot(fig)

    else:
        st.warning("Please upload the trained model.")
