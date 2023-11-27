import base64
import streamlit as st
import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_squared_error
import numpy as np
import random
import set_backgroung_image
import matplotlib.pyplot as plt

import seaborn as sns


def main():
    st.set_page_config(layout="wide")

    # st.title("# Oil Production Forecast")
    # st.markdown("<h1 style='text-align: center; color: #3498db;'>Oil Production Forecast</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #FFFF;'>Oil Production Forecast</h1>", unsafe_allow_html=True)



    # img_path_heading = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 5\FP2\Final Prophet Model-20231116T165547Z-001\Final Prophet Model\Project\heading.png"
    # img_heading = open(img_path_heading, "rb").read()
    # st.image(img_heading, use_column_width=False, width=390)

    # # Center-align the image and remove extra space
    # html_code = f'<p style="text-align:center; margin-top: 0px; margin-bottom: 0px;"><img src="data:image/png;base64,{base64.b64encode(img_heading).decode()}" alt="Heading Image"></p>'

    # st.markdown(html_code, unsafe_allow_html=True)

    #Setting the background image
    # set_backgroung_image.set_backgroung_image()

    df = pd.read_csv(r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 5\FP2\Final Prophet Model-20231116T165547Z-001\Final Prophet Model\oil_prod_data.csv");

    unique_countries = df['Geography'].explode().unique().tolist()

    # st.markdown("***Select a country of your choice:***")
    default_country = "Select a country"
    country_options = [default_country] + [str(base) for base in unique_countries]

    selected_country = st.selectbox(
        "Select a country of your choice:",
        country_options
    )

    default_ep = "Select an energy product"
    energy_product_options = [ "Crude Oil", "NGL", "Other"]


    selected_energy_product = st.radio(
        "Select an energy product:",
        energy_product_options
    )


    df_new = df
    if selected_country != default_country:
        df_new = df[df['Geography'] == selected_country]
        # st.write(f"Data for {selected_country}:\n", selected_data)
    # else:
    #     st.write("Please select a country.")

    # Rename columns
    df_new.rename(columns={'Date': 'Month', 'Value': 'US Total',
                       'ENERGY_PRODUCT:Energy product':'Product_type','Geography':'Country'}, inplace=True)


    df_new['Product_type'] = df_new['Product_type'].apply(lambda x: x.split(':')[1])

    # Convert 'Date' column to datetime
    df_new['Month'] = pd.to_datetime(df_new['Month'])
    # Reset the index to start from 0
    df_new.reset_index(drop=True, inplace=True)
    merged_df_US_Crude_Oil_forecast = pd.read_csv(r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 5\FP2\Final Prophet Model\Merged_df_US_Crude_Oil_Forecast.csv")
    merged_df_US_NGL_Oil_forecast = pd.read_csv(r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 5\FP2\Final Prophet Model\Merged_df_US_NGL_Oil_Forecast.csv")
    merged_df_US_Other_Oil_forecast = pd.read_csv(r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 5\FP2\Final Prophet Model\Merged_df_US_Other_Oil_Forecast.csv")



    if (selected_energy_product == 'Crude Oil'):
        merged_df = merged_df_US_Crude_Oil_forecast
    elif (selected_energy_product == 'NGL'):
        merged_df = merged_df_US_NGL_Oil_forecast
    else:
        merged_df = merged_df_US_Other_Oil_forecast





    #Create filter dataset for Crude
    df_crude=df_new[df_new['Product_type']=='Crude oil']
    # Remove extra colmns

    df_crude.drop(['Country','Product_type'],axis=1,inplace=True)
    # Fill null values in case of NaN

    df_crude.fillna(method='bfill',inplace=True)
    df_crude['US Total'] = np.log(df_crude['US Total'])  # Apply log transformation

    with st.container():
        col1, col2  = st.columns(2)
        with col1:
            if (selected_energy_product == 'Crude Oil'):
                merged_df = merged_df_US_Crude_Oil_forecast
                st.title("US Crude Oil Production - BPD")

            elif (selected_energy_product == 'NGL'):
                merged_df = merged_df_US_NGL_Oil_forecast
                st.title("US NGL Oil Production - BPD")
            else:
                merged_df = merged_df_US_Other_Oil_forecast
                st.title("US Other Oil Production - BPD")



            # Plot using Seaborn and Matplotlib
            plt.figure(figsize=(12.5, 7))
            sns.lineplot(data=df_new[df_new['Product_type'] == 'Crude oil'], x="Month", y="US Total")
            plt.title(selected_country+"Crude Oil Production - BPD")
            plt.grid(True)

            # Display the plot in Streamlit
            st.pyplot(plt)

        with col2:
            if (selected_energy_product == 'Crude Oil'):
                merged_df = merged_df_US_Crude_Oil_forecast
                st.title("US Crude Oil Production - KBD")

            elif (selected_energy_product == 'NGL'):
                merged_df = merged_df_US_NGL_Oil_forecast
                st.title("US NGL Oil Production - KBD")

            else:
                merged_df = merged_df_US_Other_Oil_forecast
                st.title("US Other Oil Production - KBD")

            # st.title("US Crude Oil Production - KBD")
            plt.figure(figsize=(12.5,7))
            # plot expected vs actual
            plt.plot(merged_df['ds'],merged_df['y'], label='Actual')
            plt.plot(merged_df['ds'],merged_df['yhat'], label='Predicted')
            plt.title("US Oil Production - KBD")
            plt.grid(True)
            plt.legend()
            # plt.show()
            st.pyplot(plt)




    # Plot the graph of this data to get an understanding of how well forecast looks
    # model.plot(forecast);
    # plt.title("US Crude Oil Production Forecast - KBD")
    # plt.show()
    # st.pyplot(plt)


if __name__ == "__main__":
    main()