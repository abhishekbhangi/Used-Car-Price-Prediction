import numpy as np
import pickle
import pandas as pd
import streamlit as st 

# from PIL import Image


pickle_in = open("car_price.pkl","rb")
car_price=pickle.load(pickle_in)


def welcome():
    return "Welcome All"

def predict_authentication(vehicle_age,km_driven,mileage,engine,max_power,seats):   
    prediction=car_price.predict([[vehicle_age,km_driven,mileage,engine,max_power,seats]])
    return prediction



def main():
    st.title("Car Price Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Car Mileage Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    vehicle_age = st.number_input("vehicle_age",min_value=0)
    km_driven = st.number_input("km_driven",min_value=0)
    mileage = st.number_input("mileage",min_value=0)
    engine = st.number_input("engine",min_value=0)
    max_power = st.number_input("max_power",min_value=0)
    seats = st.number_input("seats",min_value=0)
    result=""
    if st.button("Predict"):
        result=predict_authentication(vehicle_age,km_driven,mileage,engine,max_power,seats)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()