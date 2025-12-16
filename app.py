
import streamlit as st  # frontend UI design
import numpy as np
import joblib
model = joblib.load('house_price_prediction_model.pkl')
st.title('House Price Prediction')   # main title
st.write('Enter inputs to predict estimated price for your house !')  # subtitle

area_sqft = st.number_input('Area in Square Feet',min_value=200.0,max_value=10000.0,value=1200.0,step=50.0)
bedrooms = st.number_input('Number of Bedrooms',min_value=1,max_value=10,value=1,step=1)
bathrooms = st.number_input('Number of Bathrooms',min_value=1,max_value=10,value=1,step=1)
age_years = st.number_input('Age of House in Years',min_value=0.0,max_value=100.0,value=10.0,step=1.0)
distance_city_km = st.number_input('Distance to City in KM',min_value=01.0,max_value=600.0,value=12.0,step=0.5)


if st.button('Perdict Price'):
  X = np.array([[area_sqft,bedrooms,bathrooms,age_years,distance_city_km]])
  pred = model.predict(X)[0]
  st.success(f'Estimated Price : {pred:.2f}')   # print only if the model got successful
