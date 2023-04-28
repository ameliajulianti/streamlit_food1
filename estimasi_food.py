import pickle
import streamlit as st

model = pickle.load(open('estimasi_food.sav', 'rb'))

st.title('Estimasi Jumlah protein makanan ')
DataAsh = st.number_input('input Data.Ash')
DataCarbohydrate = st.number_input('Data.Carbohydrate')
DataKilocalories = st.number_input('input jumlah Data.Kilocalories')
DataCholesterol = st.number_input('input jumlah Data.Cholesterol')
DataCholine = st.number_input('input jumlah Data.Choline')
DataSelenium = st.number_input('input jumlah Data.Selenium')
DataWater = st.number_input('input jumlah data.Water')

predict = ''

if st.button('Estimasi protein'):
    predict = model.predict(
        [[DataAsh, DataCarbohydrate, DataKilocalories, DataCholesterol, DataCholine, DataSelenium, DataWater]]
        )
    st.write ('Estimasi Jumlah protein makanan : ', predict)