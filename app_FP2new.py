# app.py
# app.py

import streamlit as st
from PIL import Image
import os



# Function to get the absolute path based on the script's location
def get_absolute_path(relative_path):
    image_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Image")
    return os.path.join(image_directory, relative_path)



st.title('Oil Production Forecast')

# Display an image related to oil production forecast
oil_production_img_path = get_absolute_path("oil_production_image.PNG")
#print("Absolute path:", oil_production_img_path)
oil_production_img = Image.open(oil_production_img_path)
st.image(oil_production_img, use_column_width=True)

# Separator line for better visual separation
st.markdown("---")

# TAKE COUNTRY INPUT
country = st.text_input("Enter country")

# TAKE ENERGY PRODUCT INPUT
energy_product = st.radio('Select the energy product:', ('Crude oil', 'NGL', 'Other'))

# Display Image based on energy product selection and provided image path
show_models_results = st.button('Show Models Results')

if show_models_results:
    if energy_product == 'Crude oil':
        # 2nd Image: GluonTS Simple Feed Forward Model on validation data
        img_simple_feedforward = Image.open(get_absolute_path("GluonTS Simple Feed Forward Model on Validation Data.PNG"))
        st.header("GluonTS Simple Feed Forward Model on Validation Data")
        st.image(img_simple_feedforward, use_column_width=True)

        # 3rd Image: GluonTS DeepAR Model on Validation Data
        img_deepar = Image.open(get_absolute_path("GluonTS DeepAR Model on Validation Data.PNG"))
        st.header("GluonTS DeepAR Model on Validation Data")
        st.image(img_deepar, use_column_width=True)

        # 4th Image: Comparison GluonTS Simple FeedForward Model and Deep AR Model Forecasting on the validation Dataset
        img_comparison = Image.open(get_absolute_path("Comparison GluonTS Simple FeedForward Model and Deep AR Model Forecasting on Validation Dataset.PNG"))
        st.header("Comparison GluonTS Simple FeedForward Model and Deep AR Model Forecasting on Validation Dataset")
        st.image(img_comparison, use_column_width=True)

        # 5th Image: Validation Metrics of simple FFE and DeepAR Model
        img_metrics = Image.open(get_absolute_path("Validation Metrics of Simple FeedForward and DeepAR Model.PNG"))
        st.header("Validation Metrics of Simple FeedForward and DeepAR Model")
        st.image(img_metrics, use_column_width=True)

        # 6th Image: GluonTS Simple FeedForward Estimator model forecast on test dataset
        img_forecast = Image.open(get_absolute_path("Prophet_crude_oil_production_plot.png"))
        st.header("Prophet Model Results")
        st.image(img_forecast, use_column_width=True)

        # Read and display metrics results from the saved file
        metrics_file_path = get_absolute_path("metrics_results.txt")
        st.subheader("Metrics Results")
        try:
            with open(metrics_file_path, 'r') as file:
                metrics_content = file.read()
                st.text(metrics_content)
        except FileNotFoundError:
            st.warning("Metrics results file not found.")

        # 7th Image: LSTM model
        img_forecast = Image.open(get_absolute_path("LSTM.PNG"))
        st.header("LSTM Model Results")
        st.image(img_forecast, use_column_width=True)

        # Read and display metrics results from the saved file
        metrics_file_path = get_absolute_path("LSTM_matrix.txt")
        st.subheader("Metrics Results")
        try:
            with open(metrics_file_path, 'r') as file:
                metrics_content = file.read()
                st.text(metrics_content)
        except FileNotFoundError:
            st.warning("Metrics results file not found.")

       

elif energy_product == 'NGL':
    
        img_NGL = Image.open(get_absolute_path("Prophet_NGL_oil_production_plot.png"))
        st.header("Prophet Model Results for NGL")
        st.image(img_NGL, use_column_width=True)

        # Read and display metrics results from the saved file
        metrics_file_path = get_absolute_path("metrics_results2.txt")
        st.subheader("Metrics Results for NGL")

        try:
            with open(metrics_file_path, 'r') as file:
                    metrics_content = file.read()
                    st.text(metrics_content)
        except FileNotFoundError:
            st.warning("Metrics results file not found.")

        # 2nd Image: GluonTS Simple Feed Forward Model on validation data
        img_simple_feedforward = Image.open(get_absolute_path("Arima.PNG"))
        st.header("ARIMA & SARIMA Model Forecasting")
        st.image(img_simple_feedforward, use_column_width=True)

        # 3rd Image: GluonTS Simple Feed Forward Model on validation data
        img_simple_feedforward = Image.open(get_absolute_path("Sarima.PNG"))
        st.header("SARIMA Model Forecasting")
        st.image(img_simple_feedforward, use_column_width=True)


elif energy_product == 'Other':
        
  
        img_Other = Image.open(get_absolute_path("US_others.PNG"))
        st.header("Prophet Model Results for Others")
        st.image(img_Other, use_column_width=True)

        # Read and display metrics results from the saved file
        metrics_file_path = get_absolute_path("Others_matrix.txt")
        st.subheader("Metrics Results")

        try:
            with open(metrics_file_path, 'r') as file:
                    metrics_content = file.read()
                    st.text(metrics_content)
        except FileNotFoundError:
            st.warning("Metrics results file not found.")

        
        





 


