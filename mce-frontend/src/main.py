import streamlit as st
import requests
from src.config import API_URL

# Streamlit app title
st.title("Ma Capacité d'Emprunt")

# Input fields for the API
st.sidebar.header("Entrer les détails")
revenus_mensuels = st.sidebar.number_input("Revenus mensuels (€)", min_value=0.0, step=100.0)
charges_mensuelles = st.sidebar.number_input("Charges mensuelles (€)", min_value=0.0, step=50.0)
duree_annees = st.sidebar.slider("Durée du prêt (années)", min_value=5, max_value=30, value=20)
taux_endettement = 0.35
taux_annuel = st.sidebar.slider("Taux annuel (%)", min_value=0.1, max_value=10.0, value=1.0) / 100

# Button to calculate
if st.sidebar.button("Calculer"):
    # Call the backend API
    api_url = API_URL
    payload = {
        "revenus_mensuels": revenus_mensuels,
        "charges_mensuelles": charges_mensuelles,
        "duree_annees": duree_annees,
        "taux_endettement": taux_endettement,
        "taux_annuel": taux_annuel,
    }
    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success("Calcul réussi!")
            st.write(f"Mensualité maximale: {result['mensualite_max']} €")
            st.write(f"Capacité d'emprunt estimée: {result['capacite']} €")
        else:
            st.error(f"Erreur lors de l'appel à l'API: {response.status_code}")
    except Exception as e:
        st.error(f"Une erreur est survenue: {e}")