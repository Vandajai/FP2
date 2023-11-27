# app.py

import streamlit as st
import pickle
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet
#import tensorflow as tf
#from tensorflow import keras
#from gluonts.model.simple_feedforward import SimpleFeedForwardEstimator
#from gluonts.model.deepar import DeepAREstimator
from PIL import Image


def add_numbers(a, b):
    """
    Adds two numbers and returns the sum.
    
    Parameters:
    - a (int): The first number.
    - b (int): The second number.
    
    Returns:
    int: The sum of the two numbers.
    """
    return a + b

# Load the pickle files (replace with actual file paths)
# arima_model = pickle.load(open("US_Crude_arimaModel.pkl", "rb"))
prophet_model = pickle.load(open("US_Crude_prophetModel.pkl", "rb"))
# lstm_model = keras.models.load_model("US_Crude_lstmModel.h5")  # Replace with your actual file path
# simple_feedforward_model = SimpleFeedForwardEstimator.load("US_Crude_simple_feedforwardModel")  # Replace with your actual file path
# deepar_model = DeepAREstimator.load("US_Crude_deeparModel")  # Replace with your actual file path

# Example input data (replace with your actual data)
input_data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Streamlit UI
st.title('Oil Production Forecast')

# Display an image related to oil production forecast (if needed)
oil_production_img_path = "C:/Users/Admin/OneDrive - LTI/Desktop/Foundation _project2/Image/oil_production_image.png"
oil_production_img = Image.open(oil_production_img_path)
st.image(oil_production_img, use_column_width=True)

# Separator line for better visual separation
st.markdown("---")

# TAKE COUNTRY INPUT
country = st.text_input("Enter country")

# TAKE ENERGY PRODUCT INPUT
energy_product = st.radio('Select the energy product:',
                         ('Crude oil', 'NGL', 'Other'))

# Model Inference and Display Results based on user selection
if st.button('Show Model Results'):
    # Create a radio button to select the model
    selected_model = st.radio(
        'Select the model:', ('Prophet Model', 'ARIMA Model', 'LSTM Model', 'Simple Feed Forward Model', 'DeepAR Model'))

    if energy_product == 'Crude oil':
        if selected_model == 'Prophet Model':
            # Prophet Model
            st.subheader("Prophet Model Results")
            prophet_results_img_path = add_numbers(2,3)
            prophet_results_img = Image.open(prophet_results_img_path)
            st.image(prophet_results_img, caption="Prophet Model Results", use_column_width=True)

            # Read and display metrics results from the saved file
            metrics_file_path = "metrics_results.txt"
            st.subheader("Metrics Results")

            try:
                with open(metrics_file_path, 'r') as file:
                    metrics_content = file.read()
                    st.text(metrics_content)
            except FileNotFoundError:
                st.warning("Metrics results file not found.")
        else:
            # Display warning for other models
            st.warning(f"{selected_model} is not implemented yet.")

    elif energy_product == 'NGL':
        if selected_model == 'Prophet Model':
            # Prophet Model for NGL
            st.subheader("Prophet Model Results for NGL")
            prophet_results_img_path = "Prophet_NGL_oil_production_plot.png"
            prophet_results_img = Image.open(prophet_results_img_path)
            st.image(prophet_results_img, caption="Prophet Model Results for NGL", use_column_width=True)

            # Read and display metrics results from the saved file
            metrics_file_path = "metrics_results2.txt"
            st.subheader("Metrics Results for NGL")

            try:
                with open(metrics_file_path, 'r') as file:
                    metrics_content = file.read()
                    st.text(metrics_content)
            except FileNotFoundError:
                st.warning("Metrics results file not found.")

        elif selected_model == 'Other Model for NGL':
            # Other Model for NGL
            st.warning("Other Model for NGL is not implemented yet.")

    # Add an else block to handle cases where energy_product is neither 'Crude oil' nor 'NGL'
    else:
        st.warning("Please select a valid energy product.")








