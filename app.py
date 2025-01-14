import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
@st.cache_data
def load_data():
    return pd.read_csv('Shopping_trends.csv')

df = load_data()

st.title("Analyse des tendances d'achat")

# Affichage des informations de base
st.header("Aperçu du dataset")
st.write(f"Nombre de lignes : {df.shape[0]}, Nombre de colonnes : {df.shape[1]}")
st.dataframe(df.head())

# Statistiques descriptives
st.header("Statistiques descriptives")
st.write(df.describe())

# Analyse des colonnes catégorielles
st.header("Analyse des colonnes catégorielles")
categorical_col = st.selectbox("Choisissez une colonne catégorielle", ['Gender', 'Location', 'Season'])
st.write(df[categorical_col].value_counts())

# Montant total des achats par client
st.header("Montant total des achats par client")
total_purchase = df.groupby('Customer ID')['Purchase Amount (USD)'].sum().sort_values(ascending=False)
st.bar_chart(total_purchase.head(10))

# Montant moyen des achats par catégorie
st.header("Montant moyen des achats par catégorie")
avg_purchase = df.groupby('Category')['Purchase Amount (USD)'].mean().sort_values(ascending=True)
st.bar_chart(avg_purchase)


# One-hot encoding pour la saison
st.header("One-hot encoding pour la saison")
season_encoded = pd.get_dummies(df['Season'], prefix='Season')
st.write(season_encoded.head())

# Téléchargement des données en JSON
st.header("Télécharger les données")
json_data = df.to_json(orient='records')
st.download_button(
    label="Télécharger en JSON",
    data=json_data,
    file_name="shopping_trends.json",
    mime="application/json"
)
