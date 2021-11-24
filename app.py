import streamlit as st
import pandas as pd
from utils import *

st.title("Application de routage des camions - LPD")

uploaded_file = st.file_uploader("Choisir un fichier de commandes")
delay = st.slider("Choisir un délai de livraison", min_value=1, max_value=2)

if st.button('Calculer les routes'):
    if uploaded_file is None:
        st.text_area("Fichier invalide !")
    else:
        orders = pd.read_csv(uploaded_file)
        new_routes = optimize(orders, delay)
        st.dataframe(data=new_routes.iloc[:, 2:])
        st.download_button("Télécharger les routes", new_routes.to_csv().encode('utf-8'))