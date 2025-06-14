
import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('model_rf.pkl')

st.title("Prediksi Kategori Obesitas")

# Input form
age = st.slider("Usia", 10, 100, 25)
height = st.number_input("Tinggi badan (meter)", 1.0, 2.5, 1.65)
weight = st.number_input("Berat badan (kg)", 30.0, 200.0, 60.0)
fcvc = st.slider("Frekuensi Konsumsi Sayur (1–3)", 1, 3, 2)
ncp = st.slider("Frekuensi Makan Besar", 1, 4, 3)
ch2o = st.slider("Konsumsi Air", 1, 3, 2)
faf = st.slider("Aktivitas Fisik (jam)", 0.0, 3.0, 1.0)
tue = st.slider("Waktu Teknologi (jam)", 0.0, 2.0, 1.0)

# Buat array input
input_data = np.array([[age, height, weight, fcvc, ncp, ch2o, faf, tue]])

# Prediksi
if st.button("Prediksi"):
    prediction = model.predict(input_data)
    st.success(f"Kategori Obesitas: {prediction[0]}")
