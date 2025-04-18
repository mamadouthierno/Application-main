import streamlit as st  
import numpy as np  
import plotly.express as px  
from datetime import date  
import io  
from fpdf import FPDF  
from utils import (
    FEATURE_CONFIG,
    encode_features,
    load_model,
    predict_survival,
    clean_prediction,
    save_new_patient,
    MODELS,
    TEAM_MEMBERS
)

# Style CSS personnalisé  
st.markdown("""  
<style>  
    :root {  
        --primary: #2e77d0;  
        --secondary: #1d5ba6;  
        --accent: #22d3ee;  
    }  
    .st-emotion-cache-1y4p8pa {  
        padding: 2rem 1rem;  
    }  
    .header-card {  
        background: rgba(255, 255, 255, 0.9);  
        border-radius: 15px;  
        padding: 2rem;  
        margin: 1rem 0;  
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);  
    }  
    .prediction-card {  
        background: linear-gradient(135deg, #f8fafc, #ffffff);  
        border-left: 4px solid var(--primary);  
        padding: 1.5rem;  
        margin: 1rem 0;  
    }  
    .model-selector {  
        border-radius: 12px !important;  
        padding: 1rem !important;  
        border: 2px solid var(--primary) !important;  
    }  
    .stButton>button {  
        background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;  
        color: white !important;  
        border-radius: 8px !important;  
        padding: 0.8rem 2rem !important;  
        transition: all 0.3s !important;  
    }  
    .stButton>button:hover {  
        transform: translateY(-2px);  
        box-shadow: 0 4px 15px rgba(46, 119, 208, 0.4) !important;  
    }  
</style>  
""", unsafe_allow_html=True)  


def generate_pdf_report(input_data, cleaned_pred, model_name):  
    pdf = FPDF()  
    pdf.add_page()  
    pdf.set_font('Arial', 'B', 24)  
    pdf.set_text_color(46, 119, 208)  
    pdf.cell(0, 15, "Rapport Médical SHAHIDI-AI", ln=True, align='C')  
  
    pdf.set_font('Arial', '', 12)  
    pdf.set_text_color(0, 0, 0)  
    pdf.cell(0, 10, f"Date : {date.today().strftime('%d/%m/%Y')}", ln=True)  
  
    pdf.set_font('Arial', 'B', 16)  
    pdf.cell(0, 15, "Paramètres Cliniques", ln=True)  
    pdf.set_fill_color(240, 248, 255)  
  
    pdf.set_font('Arial', '', 12)  
    col_widths = [60, 60]  
    for key, value in input_data.items():  
        pdf.cell(col_widths[0], 8, FEATURE_CONFIG.get(key, key), 1, 0, 'L', 1)  
        pdf.cell(col_widths[1], 8, str(value), 1, 1, 'L')  
  
    pdf.set_font('Arial', 'B', 16)  
    pdf.cell(0, 15, "Résultats de Prédiction", ln=True)  
    pdf.set_font('Arial', '', 14)  
    pdf.cell(0, 8, f"Modèle utilisé : {model_name}", ln=True)  
    pdf.set_text_color(46, 119, 208)  
    pdf.cell(0, 8, f"Survie médiane estimée : {cleaned_pred:.1f} mois", ln=True)  
  
    pdf_buffer = io.BytesIO()  
    pdf.output(pdf_buffer)  
    pdf_buffer.seek(0)
    return pdf_buffer.getvalue()  


def show_model_info(selected_model):  
    """Affiche les informations du modèle sélectionné"""  
    model_info = {  
        "DeepSurv": {  
            "description": "Réseau de neurones profond pour l'analyse de survie",  
            "avantages": [  
                "Capture des relations non linéaires",  
                "Adapté aux données complexes",  
                "Mise à jour incrémentale"  
            ]  
        },  
        "CoxPH": {  
            "description": "Modèle de régression de Cox proportionnelle",  
            "avantages": [  
                "Interprétabilité statistique",  
                "Rapide pour les petites données",  
                "Standard en recherche médicale"  
            ]  
        }  
    }  

    with st.sidebar.expander("ℹ️ Info Modèle", expanded=True):  
        st.markdown(f"**{selected_model}**")  
        st.caption(model_info[selected_model]["description"])  
        st.markdown("**Avantages :**")  
        for avantage in model_info[selected_model]["avantages"]:  
            st.markdown(f"- {avantage}")  


def modelisation():  
    st.title("📊 Prédiction Intelligente de Survie")  

    # Sélection du modèle  
    model_choice = st.selectbox(  
        "Sélectionnez un modèle", ["DeepSurv", "CoxPH"],  
        index=0, key="model_choice",  
        help="Choisissez le modèle à utiliser pour prédire la survie du patient"  
    )  

    show_model_info(model_choice)  

    # Collecte des données du patient
    patient_data = {}  
    for feature, label in FEATURE_CONFIG.items():  
        patient_data[feature] = st.text_input(label, "")  

    # Encode les données et fait la prédiction
    if st.button("Faire une prédiction"):  
        encoded_data = encode_features(patient_data)  
        model = load_model(MODELS[model_choice])  
        if model is None:  
            st.error("Erreur lors du chargement du modèle.")  
            return

        try:
            prediction = predict_survival(model, encoded_data, model_choice)
            cleaned_prediction = clean_prediction(prediction)
            st.write(f"**Survie médiane estimée : {cleaned_prediction:.1f} mois**")

            # Option de rapport PDF
            if st.checkbox("Télécharger un rapport PDF"):
                pdf_data = generate_pdf_report(patient_data, cleaned_prediction, model_choice)
                st.download_button("Télécharger le rapport PDF", pdf_data, "rapport_survie.pdf")
        except Exception as e:
            st.error(f"Erreur lors de la prédiction : {e}")
