import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Sosialisasi Kode Etik BPKH")

st.title("📘 Materi Sosialisasi Kode Etik Korporasi BPKH")

with open("kode_etik.html", "r", encoding="utf-8") as f:
    html_string = f.read()

components.html(html_string, height=3000, scrolling=True)
