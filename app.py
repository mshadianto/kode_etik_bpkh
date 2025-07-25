import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide", page_title="Sosialisasi Kode Etik BPKH")

st.title("📘 Materi Sosialisasi Kode Etik Korporasi BPKH")

# File HTML kamu bernama index.html, bukan kode_etik.html
html_path = os.path.join(os.path.dirname(__file__), "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_string = f.read()

# Tampilkan dengan tinggi besar agar konten utuh
components.html(html_string, height=5000, scrolling=True)
