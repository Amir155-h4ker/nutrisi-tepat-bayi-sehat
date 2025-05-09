import streamlit as st

st.set_page_config(page_title="Beranda - Vitamin MPASI", layout="centered")

st.title("👶🍽️ Selamat Datang di Aplikasi Vitamin MPASI")

st.markdown("""
---

## 🍼 Apa Itu Aplikasi Ini?

Aplikasi ini membantu orang tua dan tenaga medis untuk:
- 🥕 Menghitung kandungan vitamin dari bahan MPASI
- 👶 Menyesuaikan dengan kebutuhan vitamin berdasarkan usia bayi
- 🍗 Merancang menu yang bergizi dan seimbang

---

## 🧭 Cara Menggunakan

1. Klik tab **Kalkulator** di sidebar kiri
2. Masukkan usia bayi
3. Pilih bahan makanan & beratnya
4. Lihat kandungan vitamin dan grafik persentase kecukupan

---

## 📌 Fitur Utama

- Kandungan vitamin dihitung dalam **miligram (mg)**
- Dapat digunakan untuk bayi usia **6–24 bulan**
- Data berdasarkan sumber resmi: **USDA, WHO, Kemenkes RI**

---

👉 Klik tab **Kalkulator** di sidebar kiri untuk mulai menghitung MPASI bayi Anda!
""")
