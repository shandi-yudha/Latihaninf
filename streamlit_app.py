import streamlit as st

st.title("Selamat Datang di Website Ini :)")
st.write(
    "Web Gabut Milik Shnydh"
)
st.image("400px-Weather_Report_Stand_Infobox_Manga.png", width=200)
st.write(
    "stand di atas stand op bernama Weather Report"
)
pip install streamlit requests beautifulsoup4
import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Web Scraper Poin-Poin")

# Input URL
url = st.text_input("Masukkan URL halaman yang ingin di-scrape:")

if url:
    try:
        response = requests.get(url)
        response.raise_for_status()  # untuk error handling
        soup = BeautifulSoup(response.text, 'html.parser')

        st.subheader("Hasil Scraping (Poin-poin)")

        # Contoh: mengambil isi <li> atau <p> pendek sebagai poin
        points = []

        # Ambil dari <li>
        for li in soup.find_all('li'):
            text = li.get_text(strip=True)
            if 30 < len(text) < 200:
                points.append(text)

        # Jika <li> tidak cukup, tambahkan <p> pendek
        if len(points) < 5:
            for p in soup.find_all('p'):
                text = p.get_text(strip=True)
                if 30 < len(text) < 200:
                    points.append(text)

        if points:
            for i, point in enumerate(points[:10], start=1):
                st.markdown(f"**{i}.** {point}")
        else:
            st.warning("Tidak ditemukan poin yang sesuai.")

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
streamlit run app.py
