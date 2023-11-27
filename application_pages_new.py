import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from math import sqrt
import os
from prophet import Prophet

# Load your data
df_new = pd.read_csv('US_Crude_Oil_Production.csv')
df_crude = df_new[df_new['Product_type'] == 'Crude oil']

# Load the pickled model and its parameters
model_filename = 'best_model_with_params.pkl'
with open(model_filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

def load_and_predict(model_filename, df_crude):
    # Load the pickled model and its parameters
    #with open(model_filename, 'rb') as model_file:
        #loaded_model = pickle.load(model_file)

    # Make future dataframe
    future = loaded_model.make_future_dataframe(periods=36, freq='m')
    future['ds'] = future['ds'].apply(lambda x: x.replace(day=1))

    # Get the forecast
    forecast = loaded_model.predict(future)

    # Print columns and head of forecast dataframe
    print("Columns in forecast:", forecast.columns)
    print("Head of forecast:")
    print(forecast.head())

    # Transform forecast values
    forecast['trend'] = np.exp(forecast['trend'])
    forecast['trend_lower'] = np.exp(forecast['trend_lower'])
    forecast['trend_upper'] = np.exp(forecast['trend_upper'])

    forecast['yhat'] = np.exp(forecast['yhat'])
    forecast['yhat_lower'] = np.exp(forecast['yhat_lower'])
    forecast['yhat_upper'] = np.exp(forecast['yhat_upper'])

    forecast['multiplicative_terms'] = np.exp(forecast['multiplicative_terms'])
    forecast['multiplicative_terms_lower'] = np.exp(forecast['multiplicative_terms_lower'])
    forecast['multiplicative_terms_upper'] = np.exp(forecast['multiplicative_terms_upper'])

    forecast['yearly'] = np.exp(forecast['yearly'])
    forecast['yearly_lower'] = np.exp(forecast['yearly_lower'])
    forecast['yearly_upper'] = np.exp(forecast['yearly_upper'])

    forecast['additive_terms'] = np.exp(forecast['additive_terms'])
    forecast['additive_terms_lower'] = np.exp(forecast['additive_terms_lower'])
    forecast['additive_terms_upper'] = np.exp(forecast['additive_terms_upper'])

    # Check for NaN or Infinite values
    if forecast.isnull().values.any() or not np.isfinite(forecast.drop(columns=['ds']).values.astype(float)).all():
        print("Warning: NaN or Infinite values detected in the forecast DataFrame.")

    forecast[["ds","yhat","yhat_lower","yhat_upper"]].head()
    # Plot the graph of this data
    loaded_model.plot(forecast)
    plt.title("US Crude Oil Production Forecast - KBD")
    plt.show()

    # Apply np.exp() to 'y' column in df_crude
    df_crude['yhat'] = np.exp(df_crude['yhat'])


    # Calculate metrics
    y_true = df_crude['yhat'][:260].values
    y_pred = forecast['yhat'][:260].values

    mae = mean_absolute_error(y_true, y_pred)
    r_squared = r2_score(y_true, y_pred)

    print('MAE: %.2f' % mae)
    print('R-squared Score: %.2f' % r_squared)

    # Merge actual and predicted dataframes
    merged_df = df_crude.merge(forecast, on='ds', how='outer')

    # Plot expected vs actual
    plt.figure(figsize=(12.5, 7))
    plt.plot(merged_df['ds'], merged_df['y'], label='Actual')
    plt.plot(merged_df['ds'], merged_df['yhat'], label='Predicted')
    plt.title("US Crude Oil Production - KBD")
    plt.grid(True)
    plt.legend()

    # Save the plot as a PNG file
    #plt.savefig("Prophet_crude_oil_production_plot.png")

    # Show the plot (optional)
    #plt.show()

    # Calculate additional metrics (RMSE and MAE)
    rmse = sqrt(mean_squared_error(y_true, y_pred))
    print("RMSE: ", rmse)
    print("MAE: ", mae)

    # Define a function to calculate MAPE
    def mean_absolute_percentage_error(y_true, y_pred):
        y_true, y_pred = np.array(y_true), np.array(y_pred)
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

    # Calculate MAPE
    mape = mean_absolute_percentage_error(y_true, y_pred)
    print("MAPE: ", mape, "%")

# Example usage
load_and_predict(model_filename, df_crude)

if __name__ == "__main__":
    # You can add additional test or utility code here if needed
    pass
