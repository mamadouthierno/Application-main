import streamlit as st
import requests
from streamlit_lottie import st_lottie
from send_email import send_email

st.set_page_config(page_title="Formulaire de Contact", page_icon=":email:", layout="centered")

# Charger l'animation Lottie
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Animation après envoi réussi
lottie_success = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

st.header("📬 Contactez-nous")
st.write("Veuillez remplir le formulaire ci-dessous :")

# Utilisation de with pour le formulaire
with st.form(key="email_form"):
    name = st.text_input("Votre nom")
    email = st.text_input("Votre adresse email")
    message = st.text_area("Votre message")
    submit_button = st.form_submit_button("Envoyer")

    if submit_button:
        if name and email and message:
            send_email(name, email, message)
            st.success("✅ Message envoyé avec succès !")
            if lottie_success:
                st_lottie(lottie_success, height=200, key="success")
        else:
            st.error("❗ Veuillez remplir tous les champs.")

