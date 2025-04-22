from PIL import Image
import streamlit as st
import os
import base64
from utils import LOGO_PATH  # On récupère le chemin défini dans utils.py

# Fonction pour convertir une image en base64 (utile pour le background)
def get_base64_bg(path):
    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

def a_propos():
    # Convertir l'image du logo en base64 pour l'utiliser comme background
    bg_image = get_base64_bg(LOGO_PATH)

    # Section HERO
    st.markdown(f"""
        <style>
            .custom-bg {{
                background-image: url("{bg_image}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 80vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
            }}
            .main-title {{
                font-size: 3rem;
                font-weight: bold;
                color: #ffffff;
                margin-bottom: 1rem;
            }}
            .sub-title {{
                font-size: 1.5rem;
                color: #ffffff;
            }}
        </style>

        <div class="custom-bg">
            <h1 class="main-title">🩺 Prévision du Temps de Survie du Cancer Gastrique</h1>
            <p class="sub-title">L'intelligence artificielle au service de l'oncologie clinique au Sénégal.</p>
        </div>
    """, unsafe_allow_html=True)

    # Statistiques clés
    st.markdown("### Principaux Indicateurs Épidémiologiques")
    cols = st.columns(3)
    stats = [
        {"icon": "🕒", "value": "58%", "label": "Survie à 5 ans"},
        {"icon": "📈", "value": "1200+", "label": "Cas annuels"},
        {"icon": "🎯", "value": "89%", "label": "Précision du modèle"}
    ]
    for col, stat in zip(cols, stats):
        with col:
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px; text-align: center; margin-bottom: 1rem;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{stat['icon']}</div>
                <div style="font-size: 2.2rem; font-weight: 700; color: #0f172a;">{stat['value']}</div>
                <div style="color: #334155; font-size: 1rem;">{stat['label']}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown('<div class="image-container">', unsafe_allow_html=True)
            st.image("assets/ibs_curve.jpeg", caption="Courbe IBS - Comparaison des modèles", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Erreur de chargement de l'image : {str(e)}")

    with col2:
        st.markdown("""
        <div style="background: rgba(white); padding: 1rem; border-radius: 10px;">
            <h3>Interprétation des Résultats</h3>
            <ul style="line-height: 1.8;">
                <li>📉 Meilleure performance du modèle Deep Survival</li>
                <li>⏱ Stabilité temporelle des prédictions</li>
                <li>🎯 Faible erreur intégrée (IBS)</li>
            </ul>
            <div style="background-color: #2e77d0; color: #fff; padding: 6px 12px; border-radius: 20px; display: inline-block; margin-top: 10px; font-size: 0.85rem;">
                🔬 Validation croisée (k=10)
            </div>
        </div>
        """, unsafe_allow_html=True)
    # Équipe de Recherche
    st.markdown("## Équipe de Recherche", unsafe_allow_html=True)
    cols = st.columns(3)
team_members = [
    {"photo": "assets/bousso.PNG", "name": "Pr. Mamadou BOUSSO", "role": "Maitre conferencier"},
    {"photo": "assets/allaya.jpeg", "name": "Dr. Mouhamad M. ALLAYA", "role": "Prof Statistique & Data Scientist"},
    {"photo": "assets/mamadou.jpg", "name": "M. Mamadou Thierno FAYE", "role": "Ingénieur Data Scientist"},
    {"photo": "assets/samb.jpeg", "name": "Dr. Fatou SAMB", "role": "Oncologue Médical"},
    {"photo": "assets/sy.jpeg", "name": "Pr. Binta SY", "role": "Épidémiologiste"}
]

for i in range(0, len(team_members), 3):
    row = team_members[i:i+3]
    cols = st.columns(len(row))
    for col, member in zip(cols, row):
        with col:
            try:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.8); text-align: center; padding: 1rem; border-radius: 10px; margin-top: 1rem; box-shadow: 0 4px 8px rgba(0,0,0,0.3);">
                    <img src="{member['photo']}" style="width: 100%; border-radius: 10px; height: 220px; object-fit: cover; border: 3px solid #2e77d0;" alt="{member['name']}">
                    <h3 style="margin: 0.5rem 0; color: #0f172a;">{member['name']}</h3>
                    <p style="margin: 0; color: #334155;">{member['role']}</p>
                    <div style="background-color: #2e77d0; color: #fff; padding: 6px 12px; border-radius: 20px; display: inline-block; margin-top: 10px; font-size: 0.85rem;">
                        🏥 CHU Thiès
                    </div>
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erreur d'affichage du profil : {str(e)}")

    # ✅ Bouton de téléchargement du PDF
    pdf_path = "assets/rapport_apropos.pdf"
    try:
        with open(pdf_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<a href="data:application/pdf;base64,{base64_pdf}" download="rapport_apropos.pdf" target="_blank" style="text-decoration:none;">📄 Télécharger le rapport complet (PDF)</a>'
            st.markdown(f"""
                <div style="margin-top: 30px; padding: 1rem; background-color: #e0f2fe; border-left: 5px solid #0284c7; border-radius: 10px;">
                    {pdf_display}
                </div>
            """, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Le fichier PDF du rapport n'a pas été trouvé.")

if __name__ == "__main__":
    a_propos()
