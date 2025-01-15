import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration du style Matplotlib
plt.style.use('dark_background')
plt.rcParams['axes.facecolor'] = 'none'
plt.rcParams['figure.facecolor'] = 'none'

@st.cache_data
def load_data():
    return pd.read_json('Shopping_trends.json')

def main():
    menu = ["Home", "Visualisations", "Conclusions", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    st.title("Analyse des tendances d'achat")

    df = load_data()

    if choice == "Home":
        st.subheader("Home")
        st.write("Bienvenue dans l'application d'analyse des tendances d'achat.")
        st.dataframe(df.head())
        

       

       
        st.header("Aperçu du dataset")
        st.write(f"Nombre de lignes : {df.shape[0]}, Nombre de colonnes : {df.shape[1]}")

        st.header("Analyse des colonnes catégorielles")
        categorical_col = st.selectbox("Choisissez une colonne catégorielle", ['Gender', 'Location', 'Season'])
        fig, ax = plt.subplots()
        df[categorical_col].value_counts().plot(kind='bar', ax=ax)
        ax.set_title(f"Distribution de {categorical_col}")
        fig.patch.set_alpha(0)
        ax.patch.set_alpha(0)
        st.pyplot(fig)

        st.header("Statistiques descriptives")
        st.write(df.describe())

        st.header("Montant total des achats par client")
        total_purchase = df.groupby('Purchase Amount (USD)')['Customer ID'].sum().sort_values(ascending=False)
        fig, ax = plt.subplots()
        ax.bar(total_purchase.head(10).index, total_purchase.head(10).values)
        ax.set_title("Top 10 des clients par montant total d'achat")
        ax.set_ylabel('Customer ID')
        ax.set_xlabel('Montant total des achats')
        fig.patch.set_alpha(0)
        ax.patch.set_alpha(0)
        st.pyplot(fig)

        st.header("One-hot encoding pour la saison")
        season_encoded = pd.get_dummies(df['Season'], prefix='Season')
        st.write(season_encoded.head())

    elif choice == "Visualisations":
        st.subheader("Visualisations avancées")

        col1, col2 = st.columns([1,1])

        with col1:
            st.header("Distribution des achats par catégorie")
            category_counts = df['Category'].value_counts()
            fig, ax = plt.subplots()
            category_counts.plot(kind='bar', ax=ax)
            ax.set_title("Distribution des achats par catégorie")
            ax.set_xlabel("Catégorie")
            ax.set_ylabel("Nombre d'achats")
            plt.xticks(rotation=45)
            fig.patch.set_alpha(0)
            ax.patch.set_alpha(0)
            st.pyplot(fig)

            st.header("Relation entre l'âge et le montant d'achat")
            fig, ax = plt.subplots()
            ax.scatter(df['Age'], df['Previous Purchases'])
            ax.set_title("Âge vs Montant d'achat")
            ax.set_xlabel("Âge")
            ax.set_ylabel("Montant d'achat")
            fig.patch.set_alpha(0)
            ax.patch.set_alpha(0)
            st.pyplot(fig)

            st.header("Proportion de clients abonnés")
            subscription_status = df['Subscription Status'].value_counts()
            fig, ax = plt.subplots()
            ax.pie(subscription_status, labels=subscription_status.index, autopct='%1.1f%%')
            ax.set_title("Proportion de clients abonnés")
            fig.patch.set_alpha(0)
            ax.patch.set_alpha(0)
            st.pyplot(fig)

        with col2:
            st.header("Distribution des notes par saison")
            fig, ax = plt.subplots()
            sns.boxplot(x='Season', y='Review Rating', data=df, ax=ax)
            ax.set_title("Distribution des notes par saison")
            ax.set_xlabel("Saison")
            ax.set_ylabel("Note")
            fig.patch.set_alpha(0)
            ax.patch.set_alpha(0)
            st.pyplot(fig)

            st.header("Fréquence d'achat par genre")
            freq_gender = pd.crosstab(df['Frequency of Purchases'], df['Gender'])
            fig, ax = plt.subplots()
            freq_gender.plot(kind='bar', stacked=True, ax=ax)
            ax.set_title("Fréquence d'achat par genre")
            ax.set_xlabel("Fréquence d'achat")
            ax.set_ylabel("Nombre de clients")
            ax.legend(title="Genre")
            fig.patch.set_alpha(0)
            ax.patch.set_alpha(0)
            st.pyplot(fig)

            st.header("Tendance des achats précédents")
            prev_purchases = df.groupby('Customer ID')['Previous Purchases'].mean().sort_values(ascending=False)
            fig, ax = plt.subplots()
            ax.plot(prev_purchases.index[:50], prev_purchases.values[:50])
            ax.set_title("Tendance des achats précédents (Top 50 clients)")
            ax.set_xlabel("ID Client")
            ax.set_ylabel("Nombre moyen d'achats précédents")
            fig.patch.set_alpha(0)
            ax.patch.set_alpha(0)
            st.pyplot(fig)

        

        # st.header("Télécharger les données")
        # json_data = df.to_json(orient='records')
        # st.download_button(
        #     label="Télécharger en JSON",
        #     data=json_data,
        #     file_name="shopping_trends.json",
        #     mime="application/json"
        # )

    elif choice == "Conclusions":
        st.subheader("Conclusions et Insights")
        st.write("Résumé des principales observations :")
        st.write("1. Les catégories les plus populaires sont...")
        st.write("2. La majorité des clients sont...")
        st.write("3. Il existe une corrélation entre...")
        st.write("4. Les tendances saisonnières montrent...")
        st.write("5. Les clients fidèles ont tendance à...")

        st.write("Ces insights peuvent être utilisés pour :")
        st.write("- Adapter les stratégies marketing par saison")
        st.write("- Cibler les promotions vers certaines catégories de produits")
        st.write("- Améliorer les programmes de fidélisation")
        st.write("- Personnaliser l'expérience client en fonction de l'âge et du genre")

    else:
        st.subheader("About")
        st.write("Cette application analyse les tendances d'achat à partir du dataset 'Shopping_trends_dataset'.")

if __name__ == "__main__":
    main()
