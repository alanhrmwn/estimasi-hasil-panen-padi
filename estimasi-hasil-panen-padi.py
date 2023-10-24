import pickle
import streamlit as st

model = pickle.load(open('estimasi-hasil-panen-padi.sav', 'rb'))

st.title('Estimasi Hasil Panen Padi di Sumatera')

Luas_Panen = st.number_input('Luas Pertanian (hektar)')
Curah_hujan = st.number_input('Jumlah rata-rata curah hujan dalam setahun (milimeter)')
Kelembapan = st.number_input('Tingkat kelembaban rata-rata dalam setahun (persentase)')
Suhu_rata_rata = st.number_input('Derajat suhu rata-rata dalam setahun (celsius)')

predict = ''

if st.button('Estimasi Hasil Panen'):
    predict = model.predict(
        [[Luas_Panen, Curah_hujan, Kelembapan, Suhu_rata_rata]]
    )
    st.write ('Estimasi Hasil Panen Padi (ton) : ', predict)
