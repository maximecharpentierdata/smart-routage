import streamlit as st
import pandas as pd
from utils import *

st.set_page_config(page_title="Smart-Routage")

st.title("Calcul des routes - LPD")
st.sidebar.header("Smart-Routage")

uploaded_file = st.sidebar.file_uploader("Choisir un fichier de commandes")
warehouse = st.sidebar.selectbox("Choisir un entrepôt", [None, "Cergy", "Rennes", "Épinal", "Montauban", "Avignon"])

if uploaded_file and warehouse:
    if st.button("Calculer les routes"):
        if uploaded_file is None:
            st.text_area("Fichier invalide !")
        else:
            orders = pd.read_csv(uploaded_file)
            
            with st.spinner('Calcul des routes optimales 🚛  ... '):
                new_routes = optimize(orders, warehouse)
            
            st.success("Calcul réussi !")

            st.download_button(
                label="Exporter les routes dans un fichier .csv",
                data=new_routes.to_csv().encode("utf-8"),
                file_name="routes.csv",
                mime="text/csv",
            )

            st.write(f"{len(new_routes)} trajets à effectuer aujourd'hui !")

            for k, (i, route) in enumerate(new_routes.iterrows()):
                with st.expander(f"Trajet {k+1} : {route.total_distance:.0f} km", ):
                    st.write(f"**Arrêts** : {route.stops}")
                    st.write(f"**Commandes** : {route.orders}")
