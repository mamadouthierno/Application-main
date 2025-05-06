import streamlit as st
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration SMTP
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "votre-email@gmail.com"
EMAIL_PASSWORD = "12_SEFD"
EMAIL_RECEIVER = "mamadouthierno4@gmail.com"

def send_email(name, sender_email, message):
    """Envoie un email avec un design HTML professionnel"""
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = f"\U0001F4EC Nouveau contact MDCINE-AI : {name}"

        html = f"""
<html>
  <body style="margin: 0; font-family: 'Segoe UI', sans-serif;">
    <div style="background: #f8faff; padding: 40px;">
      <div style="max-width: 600px; margin: 0 auto; background: white; border-radius: 16px; box-shadow: 0 4px 24px rgba(0,0,0,0.08);">
        <div style="padding: 40px; text-align: center;">
          <img src="https://i.ibb.co/0Jmshvb/logo.png" alt="MED-AI Logo" style="height: 60px; margin-bottom: 30px;">
          <div style="background: linear-gradient(135deg, #2e77d0, #22d3ee); padding: 20px; border-radius: 12px;">
            <h2 style="color: white; margin: 0;">Nouveau message de {name}</h2>
          </div>
          <div style="padding: 30px 20px; text-align: left;">
            <div style="margin-bottom: 25px;">
              <p style="font-size: 16px; color: #444; margin: 8px 0;">
                <strong style="color: #2e77d0;">📧 Email :</strong><br>
                {sender_email}
              </p>
              <p style="font-size: 16px; color: #444; margin: 8px 0;">
                <strong style="color: #2e77d0;">📝 Message :</strong><br>
                <div style="background: #f8faff; padding: 15px; border-radius: 8px; margin-top: 10px;">
                  {message}
                </div>
              </p>
            </div>
            <hr style="border: 1px solid #eee; margin: 30px 0;">
            <p style="font-size: 14px; color: #888; text-align: center;">
              Ce message a été envoyé via le formulaire de contact MED-AI
            </p>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
"""




        msg.attach(MIMEText(html, "html"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

        return True
    except Exception as e:
        st.error(f"\u274C Erreur d'envoi : {str(e)}")
        return False

def validate_email(email):
    """Validation avancée d'email"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def contact():
    """Interface de contact professionnelle avec style modernisé et liens vers réseaux sociaux"""

    # Appliquer la couleur de fond globale
    st.markdown("""
        <style>
        .main-container {
            background-color: #f0f4f8;
            padding: 2rem;
            border-radius: 10px;
        }
        body {
            background-color: #f0f4f8;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)

        # En-tête
        st.markdown("""
            <div class='contact-header'>
                <h1 style="font-size: 2.5rem; margin-bottom: 1rem;">\U0001F4EC Contacte L'équipe Médicale</h1>
                <p style="font-size: 1.2rem; opacity: 0.9;">
                    Question ? Projet ? Nous répondons dans les 24h
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Grille principale
        col1, col2 = st.columns([2, 1], gap="large")

        with col1:
            with st.form("contact_form"):
                name = st.text_input("Nom Complet *", placeholder="Dr. SAMB")
                email = st.text_input("Email Professionnel *", placeholder="contact@clinique.com")
                message = st.text_area("Message *", height=200, placeholder="Décrivez votre demande en détail...")
                submitted = st.form_submit_button("Envoyer le Message ✉️", use_container_width=True)

        with col2:
            st.markdown("""
                ### 📌 Coordonnées
                **🏥 Clinique MEDICINE-AI**  
                123 Rue de la Santé, Thiès, Sénégal

                **📞 Téléphone**  
                +221 77 135 48 03 (Urgences 24/7)

                **🌐 Réseaux Sociaux**  
                🔗 [LinkedIn](https://www.linkedin.com/in/mamadouthierno)  
                🐦 [Twitter](https://twitter.com/mamadouthierno)  
                📘 [Facebook](https://www.facebook.com/mamadouthierno)
            """, unsafe_allow_html=True)

        # Validation et envoi
        if submitted:
            if not all([name, email, message]):
                st.error("\U0001F6A8 Tous les champs obligatoires (*) doivent être remplis")
            elif not validate_email(email):
                st.error("\U0001F4E7 Format d'email invalide")
            else:
                with st.spinner("Envoi en cours..."):
                    if send_email(name, email, message):
                        st.success("""
                            <div style="display: flex; align-items: center; padding: 1.5rem; background: #f0faff; border-radius: 12px; margin: 2rem 0;">
                                <div style="font-size: 2rem; margin-right: 1rem;">✅</div>
                                <div>
                                    <h3 style="margin: 0; color: #2e77d0;">Message envoyé !</h3>
                                    <p style="margin: 0.3rem 0 0; color: #666;">Nous vous répondrons dans les 24 heures</p>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                        st.balloons()

        # Carte interactive
        st.markdown("""
            <div class='map-container'>
                <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3859.227291477752!2d-17.44483768468878!3d14.693534078692495!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xec1725a1bb04215%3A0x9d5f3e9d0e8e4b1e!2sDakar!5e0!3m2!1sfr!2ssn!4v1625060000000!5m2!1sfr!2ssn" 
                    width="100%" 
                    height="400" 
                    style="border:0;" 
                    allowfullscreen="" 
                    loading="lazy">
                </iframe>
            </div>
        """, unsafe_allow_html=True)

        # Pied de page
        st.markdown("""
            <div class="footer">
                <p>
                     © 2025 <strong>MEDCINE-AI</strong> | Propulsé avec ❤️ par <strong>Mamadou Thierno FAYE</strong><br>
                    Connectez-vous avec moi :
                    <a href="https://www.linkedin.com/in/mamadouthierno" target="_blank">🔗 LinkedIn</a>
                    <a href="https://twitter.com/mamadouthierno" target="_blank">🐦 Twitter</a>
                    <a href="https://www.facebook.com/mamadouthierno" target="_blank">📘 Facebook</a>
                </p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    contact()
