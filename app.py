import streamlit as st
import pandas as pd
from utils import *

st.set_page_config(page_title="Smart-Routage")

st.title("Calcul des routes - LPD")
st.sidebar.header("Smart-Routage")

uploaded_file = st.sidebar.file_uploader("Choisir un fichier de commandes")
delay = st.sidebar.slider("Choisir un délai de livraison", min_value=1, max_value=2)

if st.button("Calculer les routes"):
    if uploaded_file is None:
        st.text_area("Fichier invalide !")
    else:
        orders = pd.read_csv(uploaded_file)
        new_routes = optimize(orders, delay)
        st.dataframe(data=new_routes.iloc[:, 2:])
        st.download_button(
            label="Télécharger les routes",
            data=new_routes.to_csv().encode("utf-8"),
            file_name="routes.csv",
            mime="text/csv",
        )
