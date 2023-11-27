# app.py

import streamlit as st
from PIL import Image

st.title('Oil Production Forecast')

# Display an image related to oil production forecast
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

# Image path for the second graph
graph2_img_path = "C:/Users/Admin/OneDrive - LTI/Desktop/Foundation _project2/Image/Graph1.png"

# Display Image based on energy product selection and provided image path
if energy_product == 'Crude oil':
    try:
        img = Image.open(graph2_img_path)

        # display image using streamlit
        # width is used to set the width of an image
        st.image(img, caption=f"Country: {country}", use_column_width=True)
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")

# Display additional images with headings
if st.button('Show'):
    # 2nd Image: GluonTS Simple Feed Forward Model on validation data
    img_simple_feedforward = Image.open("C:/Users/Admin/OneDrive - LTI/Desktop/Foundation _project2/Image/GluonTS Simple Feed Forward Model on Validation Data.png")
    st.header("GluonTS Simple Feed Forward Model on Validation Data")
    st.image(img_simple_feedforward, use_column_width=True)

    # 3rd Image: GluonTS DeepAR Model on Validation Data
    img_deepar = Image.open("C:/Users/Admin/OneDrive - LTI/Desktop/Foundation _project2/Image/GluonTS DeepAR Model on Validation Data.png")
    st.header("GluonTS DeepAR Model on Validation Data")
    st.image(img_deepar, use_column_width=True)

    # 4th Image: Comparison GluonTS Simple FeedForward Model and Deep AR Model Forecasting on the validation Dataset
    img_comparison = Image.open("C:/Users/Admin/OneDrive - LTI/Desktop/Foundation _project2/Image/Comparison GluonTS Simple FeedForward Model and Deep AR Model Forecasting on Validation Dataset.png")
    st.header("Comparison GluonTS Simple FeedForward Model and Deep AR Model Forecasting on Validation Dataset")
    st.image(img_comparison, use_column_width=True)

    # 5th Image: Validation Metrics of simple FFE and DeepAR Model
    img_metrics = Image.open("C:/Users/Admin/OneDrive - LTI/Desktop/Foundation _project2/Image/Validation Metrics of Simple FeedForward and DeepAR Model.png")
    st.header("Validation Metrics of Simple FeedForward and DeepAR Model")
    st.image(img_metrics, use_column_width=True)

    # 6th Image: GluonTS Simple FeedForward Estimator model forecast on test dataset
    img_forecast = Image.open("C:/Users/Admin/OneDrive - LTI/Desktop/Foundation _project2/Image/GluonTS Simple FeedForward Estimator Model Forecast on Test Dataset.png")
    st.header("GluonTS Simple FeedForward Estimator Model Forecast on Test Dataset")
    st.image(img_forecast, use_column_width=True)

    # 7th Image: GluonTS DeepARModel forecast on test dataset
    img_forecast = Image.open("C:/Users/Admin/OneDrive - LTI/Desktop/Foundation _project2/Image/GGluonTS DeepARModel forecast on test dataset.png")
    st.header("GGluonTS DeepARModel forecast on test dataset")
    st.image(img_forecast, use_column_width=True)


 


