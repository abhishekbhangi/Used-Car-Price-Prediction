import numpy as np
import pickle
import pandas as pd
import streamlit as st

# Load model
pickle_in = open("car_price.pkl", "rb")
car_price = pickle.load(pickle_in)

def predict_authentication(vehicle_age, km_driven, mileage, engine, max_power, seats):
    prediction = car_price.predict([[vehicle_age, km_driven, mileage, engine, max_power, seats]])
    return prediction


def main():
    st.set_page_config(layout="centered", page_title="Car Price Prediction")

    animated_theme = """
    <style>

    /* ======== PREMIUM SOFT ANIMATED GRADIENT BACKGROUND ======== */

    @keyframes smoothGradient {
        0% { background-position: 0% 0%; }
        50% { background-position: 100% 100%; }
        100% { background-position: 0% 0%; }
    }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(
            135deg,
            #1e3c72,
            #2a5298,
            #4b79a1,
            #283e51
        );
        background-size: 250% 250%;
        animation: smoothGradient 18s ease-in-out infinite;
        color: white;
    }

    /* Fade-in Animation */
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(25px);}
        to {opacity: 1; transform: translateY(0);}
    }
    /* Glass Card */
    .glass-card {
        animation: fadeIn 1.3s ease;
        background: rgba(255,255,255,0.07);
        padding: 30px;
        border-radius: 20px;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 0 0 30px rgba(0,0,0,0.25);
    }

   

    /* Main Title */
    .main-title {
        text-align:center;
        font-size: 42px;
        font-weight: 900;
        animation: fadeIn 1.6s ease;
        color:#e3f6ff;
        text-shadow: 0 0 12px #86c5ff;
    }

    /* Subtitle */
    .sub-title {
        text-align:center;
        font-size: 20px;
        margin-top: -12px;
        margin-bottom: 25px;
        font-weight: 600;
        color: #d4efff;
        animation: fadeIn 1.8s ease;
        text-shadow: 0 0 8px #86c5ff;
    }

    /* Hover Glow for Inputs */
    input:hover {
        border-color: #86c5ff !important;
        box-shadow: 0 0 12px #86c5ff;
        transition: 0.3s ease;
    }

    /* Buttons */
    div.stButton > button {
        background: linear-gradient(90deg, #2193b0, #6dd5ed);
        color: white;
        font-weight: 800;
        border-radius: 14px;
        padding: 10px 28px;
        transition: 0.4s;
        border: none;
    }

    @keyframes pulseGlow {
        0% {box-shadow: 0 0 12px #6dd5ed;}
        50% {box-shadow: 0 0 22px #6dd5ed;}
        100% {box-shadow: 0 0 12px #6dd5ed;}
    }

    div.stButton > button:hover {
        transform: scale(1.06);
        animation: pulseGlow 1.3s infinite;
        background: linear-gradient(90deg, #6dd5ed, #2193b0);
    }

    label, p, span {
        color: white !important;
        font-weight: 600 !important;
    }

    </style>
    """

    st.markdown(animated_theme, unsafe_allow_html=True)

    st.markdown("<h1 class='glass-card',style=text-align: center>🚗 Car Price Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>AI-powered model to estimate used car prices</p>", unsafe_allow_html=True)

    #st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

    # ============== INPUTS ==============

    col1, col2 = st.columns(2)
    with col1:
        vehicle_age = st.number_input("⏳ Vehicle Age", min_value=0.0, step=0.1, format="%.2f")
    with col2:
        km_driven = st.number_input("📍 KM Driven", min_value=0.0, step=0.1, format="%.2f")

    col3, col4 = st.columns(2)
    with col3:
        mileage = st.number_input("⛽ Mileage (km/l)", min_value=0.0, step=0.1, format="%.2f")
    with col4:
        engine = st.number_input("🔧 Engine CC", min_value=0.0, step=0.1, format="%.2f")

    col5, col6 = st.columns(2)
    with col5:
        max_power = st.number_input("⚡ Max Power", min_value=0.0, step=0.1, format="%.2f")
    with col6:
        seats = st.number_input("🪑 Seats", min_value=0.0, step=0.1, format="%.2f")

    # ============== BUTTONS SIDE BY SIDE ==============

    btn1, btn2 = st.columns(2)

    with btn1:
        predict_clicked = st.button("🔮 Predict Price")

    with btn2:
        about_clicked = st.button("ℹ️ About")

    # ============== OUTPUTS ==============

    if predict_clicked:
        result = predict_authentication(vehicle_age, km_driven, mileage, engine, max_power, seats)
        st.success(f"💰 Predicted Car Price: {result}")

    if about_clicked:
        st.info("✨ This ML App is built with Streamlit.\n⭐ Styled with premium gradients, icons & glass UI!")

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == '__main__':
    main()
