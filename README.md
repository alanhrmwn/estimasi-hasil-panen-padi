# Laporan Proyek Machine Learning
### Nama : Alan Hermawan
### Nim : 211351010
### Kelas : Malam B

## Domain Proyek

Nasi yang menjadi makanan utama di Indonesia menjadi alasan terpenting dalam produksi padi di Indonesia. Dengan adanya sistem yang membantu para petani dalam memprediksi hasil panen yang akan mereka dapatkan dapat membantu petani dalam memprediksi kapan mereka akan mendapatkan hasil panen yang mereka inginkan.

## Business Understanding

Model ini dibuat untuk mendapatkan estimasi hasil produksi/panen padi di sumatera dalam satuan ton dengan inputan :
Luas tanah pertanian (Hektar), Jumlah rata-rata curah hujan dalam setahun (milimeter), Tingkat kelembaban rata-rata dalam setahun (persentase), Derajat suhu rata-rata dalam setahun (celsius). Diharapkan model ini akan membantu petani padi sumatera untuk mengetahui estimasi hasil panen padi.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Petani yang mengalami gagal panen dikarenakan pengaruh cuaca
- Petani yang tidak mengetahui saat kondisi cuara seperti apa mereka akan mendapatkan hasil panen yang mereka inginkan
- Petani yang tidak memiliki estimasi berapa banyak hasil panen yang akan mereka dapatkan

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Dapat membantu petani dalam mendapatkan estimasi jumlah panen yang mereka dapatkan
- Petani mengetahui cuaca seperti apa yang baik untuk mereka menanam padi
- Mengurangi gagal panen petani
- 
    ### Solution statements
    - pembuatan sistem estimasi hasil panen yang dapat digunakan oleh petani agar mengurangi gagal panen atau hasil panen yang tidak sesuai dengan keinginan mereka
    - sistem yang dibuat menggunakan motode estimasi dengan algoritma regresi linear dengan akurasi minimal 75%
  
## Data Understanding
Dataset yang dipakai diambil dari kaggle yang berisi 224 baris dan 5 kolom mencakup data produksi tahunan dan luas panen padi dari 1993 hingga 2020. Selain itu terdapat data perubahan cuaca dari BMKG, termasuk curah hujan harian, kelembapan, dan suhu rata-rata.

Dataset: [Dataset Tanaman Padi Sumatera, Indonesia](https://www.kaggle.com/datasets/ardikasatria/datasettanamanpadisumatera).

### Variabel-variabel pada Dataset adalah sebagai berikut:
Provinsi: Nama provinsi (object)
Tahun : Tahun produksi padi (integer)
Produksi: Hasil produksi atau panen tahunan (ton) (float)
Luas Panen: Luas Pertanian (hektar) (float)
Curah hujan: Jumlah rata-rata curah hujan dalam setahun (milimeter) (float)
Kelembaban: Tingkat kelembaban rata-rata dalam setahun (persentase) (float)
Suhu Rata-Rata: Derajat suhu rata-rata dalam setahun (celsius) (float)

## Data Preparation
Cek missing values dalam dataset
```
sns.heatmap(df.isnull())
```

![image](https://github.com/alanhrmwn/estimasi-hasil-panen-padi/assets/148874522/9e0426c0-f78a-4e0f-b646-ebde29b8ca2f)

Dataset yang digunakan nyaris sesuai dengan kriteria dataset yang dapat di proses oleh algoritma yang dipakai maka dari itu hanya ada satu tahapan preparation yang dilakukan dalam pembuatan model ini yaitu penghapusan kolom Provinsi yang mana memiliki tipe data object dengan cara:
```bash
df = df.drop(['Provinsi','Tahun'], axis=1)
```
Cek korelasi antar kolom
![image](https://github.com/alanhrmwn/estimasi-hasil-panen-padi/assets/148874522/a7b1c694-c13c-4fdc-ae2e-4103a34ac24f)

Visualisasi hasil produksi padi per provinsi:
```
plt.figure(figsize=(15,8))
sns.barplot(x='Provinsi', y='Produksi', data=df)
plt.show()
```

![image](https://github.com/alanhrmwn/estimasi-hasil-panen-padi/assets/148874522/6fab14f2-d3b1-4598-852b-e57968614c68)

Visualisasi hasil produksi padi per tahun:
```
plt.figure(figsize=(15,8))
sns.barplot(x='Tahun',y='Produksi',data=df)
plt.xticks(rotation=45)
plt.show()
```

![image](https://github.com/alanhrmwn/estimasi-hasil-panen-padi/assets/148874522/0ebf1b93-a024-450f-addb-534d5a4ce37e)


## Modeling
1. Seleksi fitur dan label
```bash
features = ['Luas Panen', 'Curah hujan','Kelembapan', 'Suhu rata-rata']
x = df[features]
y = df['Produksi']
x.shape, y.shape
```
3. Memisahkan data training dan testing
```bash
from sklearn.model_selection import train_test_split
x_train, X_test, y_train, y_test = train_test_split(x,y,random_state=70)
y_test.shape
```
4. Pembuatan model regresi linear
```bash
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)
pred = lr.predict(X_test)
```

## Evaluation
Metrik evaluasi yang digunakan untuk mengevaluasi model yang dibuat adalah metrik akurasi:
```bash
score = lr.score(X_test, y_test)
print('akurasi model regresi linier = ', score)
```
Dengan itu, akurasi yang didapatkan adalah 86.63623649914514% yang mana menunjukan jika model yang dibuat dapat dipakai karna memiliki akurasi yang cukup tinggi.

## Deployment

[Estimasi Hasil Panen Padi](https://estimasi-panen-alan.streamlit.app/)
