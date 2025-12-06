import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Used Phone Price Predictor", page_icon="📱", layout="centered")

st.markdown("""
    <style>
        .main { background-color: #f2f2f2; }
        .title { font-size: 32px; font-weight: 800; text-align: center; margin-top: 10px; }
        .subtitle { text-align: center; color: #666; margin-bottom: 20px; }
        .stButton>button {
            background-color: #2ecc71;
            color: white;
            border-radius: 8px;
            width: 100%;
            height: 3em;
            font-size: 18px;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📱 Used Phone Price Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Estimate the resale value of any smartphone instantly</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox("Brand", ["Samsung", "Apple", "Xiaomi", "Realme", "OnePlus", "Other"])
    ram = st.number_input("RAM (GB)", min_value=1, max_value=32, value=6)
    storage = st.number_input("Storage (GB)", min_value=8, max_value=1024, value=128)
    battery = st.number_input("Battery Capacity (mAh)", min_value=1000, max_value=10000, value=4500)

with col2:
    processor_score = st.number_input("Processor Score (1–10)", min_value=1, max_value=10, value=7)
    screen_size = st.number_input("Screen Size (inches)", min_value=4.0, max_value=8.0, value=6.4, step=0.1)
    release_year = st.number_input("Release Year", min_value=2010, max_value=2025, value=2021)
    condition = st.selectbox("Condition", ["Like New", "Good", "Average", "Below Average"])

brand_map = {"Samsung": 3, "Apple": 5, "Xiaomi": 2, "Realme": 1, "OnePlus": 4, "Other": 0}
condition_map = {"Like New": 3, "Good": 2, "Average": 1, "Below Average": 0}

input_data = np.array([[ 
    brand_map[brand],
    ram,
    storage,
    battery,
    processor_score,
    screen_size,
    release_year,
    condition_map[condition]
]])

model = pickle.load(open("model.pkl", "rb"))

if st.button("Predict Price 💰"):
    price = model.predict(input_data)[0]
    st.success(f"Estimated Price: ₹ {int(price):,}")

st.markdown("<hr><div style='text-align:center; color:#777;'>Made with ❤️ using ML & Streamlit</div>", unsafe_allow_html=True)

