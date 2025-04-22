import streamlit as st

# ✅ Configuration de la page – doit être la toute première commande Streamlit
st.set_page_config(
    page_title="Gastric",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 📦 Imports restants
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from onglets import accueil, analyse_descriptive, modelisation, a_propos, contact

# 🔀 Dictionnaire des pages
PAGES = {
    "🏠 Accueil": accueil,
    "📊 Analyse": analyse_descriptive,
    "🤖 Prédiction": modelisation,
    "📚 À Propos": a_propos,
    "📩 Contact": contact
}

def main():
    st.markdown(
        """
        <style>
        .stTabs [data-baseweb="tab"] {
            justify-content: flex-end;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    tabs = st.tabs(list(PAGES.keys()))
    for tab, (page_name, page_func) in zip(tabs, PAGES.items()):
        with tab:
            page_func()

if __name__ == "__main__":
    main()
