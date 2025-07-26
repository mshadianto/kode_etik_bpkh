import streamlit as st
import streamlit.components.v1 as components
import os

# Set page config
st.set_page_config(
    layout="wide", 
    page_title="Sosialisasi Kode Etik BPKH",
    page_icon="🕌",
    initial_sidebar_state="collapsed"
)

# Custom CSS to hide Streamlit elements for fullscreen experience
st.markdown("""
<style>
    .stApp > header {
        background-color: transparent;
    }
    .stApp {
        margin: 0;
        padding: 0;
    }
    .main .block-container {
        padding: 0;
        margin: 0;
        max-width: 100%;
    }
    .stToolbar {
        display: none;
    }
    #MainMenu {
        display: none;
    }
    .stDeployButton {
        display: none;
    }
    .stDecoration {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Header info (optional - will be hidden in fullscreen)
st.title("🕌 Sosialisasi Kode Etik Korporasi BPKH")
st.markdown("**Platform Terpadu: Materi Kebijakan + Pembelajaran Interaktif**")

# Load the integrated HTML file
html_path = os.path.join(os.path.dirname(__file__), "integrated_ethics.html")

# Check if file exists
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_string = f.read()
    
    # Display with fullscreen height
    components.html(html_string, height=800, scrolling=True)
else:
    st.error("File integrated_ethics.html tidak ditemukan! Pastikan file sudah disimpan di direktori yang sama dengan app.py")
    
    # Fallback option
    st.markdown("""
    ## 📋 Instruksi Setup:
    
    1. **Simpan file HTML** yang telah dibuat dengan nama `integrated_ethics.html`
    2. **Letakkan di direktori yang sama** dengan file `app.py`
    3. **Refresh halaman** untuk melihat aplikasi terpadu
    
    ### 🔧 Struktur File:
    ```
    📁 project-folder/
    ├── app.py
    ├── integrated_ethics.html  ← File baru
    └── requirements.txt (optional)
    ```
    
    ### 🚀 Cara Menjalankan:
    ```bash
    streamlit run app.py
    ```
    """)

# Footer information
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9rem;'>
    <p><strong>Narasumber:</strong> M Sopian Hadianto | Anggota Komite Audit</p>
    <p>BPKH - Badan Pengelola Keuangan Haji | Platform Sosialisasi Interaktif</p>
</div>
""", unsafe_allow_html=True)
