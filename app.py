import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Dashboard E-commerce",
    page_icon="📊",
    layout="wide"
)

# Fonction de chargement des données depuis la base SQLite local
@st.cache_data
def load_data():
    conn = sqlite3.connect('analysis.db')
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()
    return df

df = load_data()

# ---------------------------------------------------------
# BARRE LATÉRALE - FILTRES INTERACTIFS
# ---------------------------------------------------------
st.sidebar.header("🔍 Filtres interactifs")

# Filtre par Pays
countries = ['Tous'] + sorted(df['Country'].unique().tolist())
selected_country = st.sidebar.selectbox("Sélectionner un pays :", countries)

# Filtrer le DataFrame selon le choix
if selected_country != 'Tous':
    filtered_df = df[df['Country'] == selected_country]
else:
    filtered_df = df.copy()

# ---------------------------------------------------------
# ENTÊTE & RÉSUMÉ EXÉCUTIF
# ---------------------------------------------------------
st.title("📊 Tableau de Bord d'Analyse Commerciale E-Commerce")
st.markdown("""
### 📌 Résumé Exécutif
Ce tableau de bord interactif présente les performances commerciales globales, la segmentation client et la répartition géographique des ventes à partir des données nettoyées enregistrées dans `analysis.db`.
""")

# Métriques clés (KPIs)
st.subheader("Indicateurs Clés de Performance (KPIs)")
col1, col2, col3, col4 = st.columns(4)

total_sales = filtered_df['TotalPrice'].sum()
total_orders = filtered_df['InvoiceNo'].nunique()
total_customers = filtered_df['CustomerID'].nunique()
avg_order_value = total_sales / total_orders if total_orders > 0 else 0

col1.metric("Chiffre d'Affaires Total", f"{total_sales:,.2f} €")
col2.metric("Commandes Totales", f"{total_orders:,}")
col3.metric("Nombre de Clients", f"{total_customers:,}")
col4.metric("Panier Moyen", f"{avg_order_value:,.2f} €")

st.divider()

# ---------------------------------------------------------
# CONCLUSIONS CLÉS & GRAPHIQUE INTERACTIFS
# ---------------------------------------------------------
st.subheader("📈 Conclusions Clés & Visualisations")

tab1, tab2 = st.tabs(["Tendance Temporelle", "Top Marchés"])

with tab1:
    st.markdown("**Évolution mensuelle du chiffre d'affaires**")
    monthly_sales = filtered_df.groupby('Month')['TotalPrice'].sum().reset_index()
    
    fig_line = px.line(
        monthly_sales, 
        x='Month', 
        y='TotalPrice', 
        labels={'Month': 'Mois', 'TotalPrice': 'Chiffre d\'Affaires (€)'},
        markers=True,
        template="plotly_white"
    )
    st.plotly_chart(fig_line, use_container_width=True)

with tab2:
    st.markdown("**Top 10 des Pays par Chiffre d'Affaires (hors UK)**")
    df_no_uk = df[df['Country'] != 'United Kingdom']
    top_countries = df_no_uk.groupby('Country')['TotalPrice'].sum().nlargest(10).reset_index()
    
    fig_bar = px.bar(
        top_countries, 
        x='TotalPrice', 
        y='Country', 
        orientation='h',
        labels={'Country': 'Pays', 'TotalPrice': 'CA (€)'},
        color='TotalPrice',
        color_continuous_scale='Blues',
        template="plotly_white"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# ---------------------------------------------------------
# RECOMMANDATIONS STRATÉGIQUES
# ---------------------------------------------------------
st.subheader("💡 Recommandations Stratégiques pour l'Entreprise")

st.info("""
- **Saisonnalité :** Intensifier les campagnes marketing dès la fin de l'été pour maximiser le pic de ventes constaté au dernier trimestre.
- **Expansion Internationale :** Cibler en priorité les Pays-Bas, l'Irlande (EIRE) et l'Allemagne avec des campagnes localisées et un support dédié.
- **Fidélisation Client :** Mettre en place un programme VIP réservé aux clients du segment *Champions* afin de sécuriser le panier moyen élevé.
""")