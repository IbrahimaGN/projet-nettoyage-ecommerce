# E-commerce Data Analytics Dashboard

> Projet d'analyse de données e-commerce avec Python, Pandas, SQL et
> Streamlit.

## Démo en ligne

**Accéder au dashboard :** <https://ecommerce-dapython.streamlit.app/>

## Présentation du projet

Ce projet consiste à exploiter des données e-commerce afin d'en extraire
des informations utiles à la compréhension des ventes et du comportement
des clients. Il couvre les principales étapes d'un processus de Data
Analytics, depuis la préparation des données jusqu'à la mise à
disposition des résultats dans un tableau de bord web interactif.

L'objectif est de transformer des données brutes en indicateurs et
visualisations faciles à explorer pour faciliter l'analyse et la prise
de décision.

## Objectifs

-   Préparer et fiabiliser les données avant leur analyse.
-   Explorer les données à l'aide de Python et Pandas.
-   Réaliser des analyses agrégées avec SQL et SQLite.
-   Présenter les résultats à l'aide de visualisations.
-   Approfondir l'analyse des ventes ou des clients avec une méthode
    adaptée aux données.
-   Déployer un dashboard interactif accessible en ligne.

## Fonctionnalités et étapes du projet

### 1. Nettoyage et préparation des données

-   Chargement des données dans un DataFrame Pandas.
-   Vérification et traitement des doublons.
-   Contrôle des types de données et conversion des dates lorsque
    nécessaire.
-   Standardisation des champs textuels.
-   Vérification des valeurs incohérentes et des anomalies métier.
-   Export des données préparées pour les étapes suivantes.

### 2. Analyse SQL

-   Chargement des données préparées dans une base SQLite.
-   Écriture de requêtes SQL pour agréger et explorer les données.
-   Analyse de dimensions métier telles que les ventes, les périodes,
    les pays et les clients, selon les champs disponibles.

### 3. Visualisation des données

-   Création de graphiques adaptés aux questions d'analyse.
-   Utilisation de visualisations pour comparer les catégories, suivre
    les évolutions temporelles et comprendre les distributions.
-   Présentation des principaux enseignements issus des graphiques.

### 4. Analyse approfondie

Une analyse avancée est réalisée en fonction des données disponibles,
par exemple une segmentation RFM, une analyse de cohortes ou une analyse
de corrélation.

### 5. Dashboard interactif

-   Mise à disposition des résultats dans une application Streamlit.
-   Affichage d'indicateurs et de graphiques d'analyse.
-   Exploration des données au moyen des filtres disponibles dans
    l'application.
-   Déploiement public sur Streamlit Community Cloud.

> Les indicateurs exacts, les filtres et les analyses disponibles sont
> ceux qui sont effectivement implémentés dans la version en ligne du
> dashboard.

## Technologies utilisées

-   **Python** --- langage d'analyse et de traitement des données
-   **Pandas / NumPy** --- manipulation et préparation des données
-   **SQLite / SQL** --- requêtes et agrégations
-   **Matplotlib / Seaborn** --- visualisation exploratoire
-   **Streamlit** --- application web interactive
-   **Plotly** --- visualisations interactives, si utilisé dans
    l'application
-   **Jupyter Notebook** --- exploration et documentation des analyses
-   **Git / GitHub** --- versionnement et partage du projet
-   **Streamlit Community Cloud** --- déploiement en ligne

## Accéder au projet

Le dashboard est accessible sans installation :

👉 **[Ouvrir le dashboard
E-commerce](https://ecommerce-dapython.streamlit.app/)**

## Installation et lancement en local

### Prérequis

-   Python 3.10 ou une version compatible avec les dépendances du projet
-   Git (facultatif, pour cloner le dépôt)

### 1. Cloner le dépôt

Remplacez `URL_DU_DEPOT_GITHUB` par l'URL réelle de votre dépôt :

``` bash
git clone URL_DU_DEPOT_GITHUB
cd NOM_DU_DEPOT
```

### 2. Créer un environnement virtuel

Sous Windows :

``` bash
python -m venv .venv
.venv\Scripts\activate
```

Sous macOS ou Linux :

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installer les dépendances

Si le dépôt contient un fichier `requirements.txt` :

``` bash
pip install -r requirements.txt
```

Sinon, installez les bibliothèques nécessaires au projet :

``` bash
pip install streamlit pandas numpy matplotlib seaborn plotly openpyxl
```

### 4. Lancer l'application

Depuis le répertoire contenant `app.py` :

``` bash
streamlit run app.py
```

Streamlit affichera l'adresse locale à ouvrir dans votre navigateur.

## Structure indicative du dépôt

La structure exacte dépend de l'organisation du dépôt. Une organisation
possible est :

``` text
ecommerce-data-analytics/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
├── notebooks/
│   ├── 01_clean_and_structure.ipynb
│   ├── 02_sql_analysis.ipynb
│   ├── 03_visualizations.ipynb
│   └── 04_deeper_analysis.ipynb
└── analysis.db
```

Les noms et fichiers ci-dessus sont indicatifs : conservez uniquement
ceux qui existent réellement dans votre dépôt. Évitez de publier des
données confidentielles ou volumineuses si elles ne sont pas nécessaires
à l'exécution.

## Résultats attendus

À l'issue de ce projet, l'utilisateur peut consulter une application en
ligne pour explorer les analyses e-commerce. Le travail met en pratique
plusieurs compétences complémentaires : préparation des données,
requêtes SQL, visualisation, analyse exploratoire et création d'une
application analytique.

Pour les conclusions métier et les chiffres précis, consultez
directement le dashboard :
[ecommerce-dapython.streamlit.app](https://ecommerce-dapython.streamlit.app/).

## Pistes d'amélioration

Selon les besoins et les données disponibles, le projet peut évoluer
avec : - de nouveaux indicateurs de performance (KPI) ; - des filtres
supplémentaires ; - une analyse plus détaillée de la fidélisation et de
la rétention ; - l'automatisation de la mise à jour des données ; - des
tests et une documentation technique complémentaires.

## Auteur

Projet personnel de Data Analytics.

## Licence

Aucune licence n'est spécifiée dans ce README. Ajoutez un fichier
`LICENSE` si vous souhaitez définir explicitement les conditions de
réutilisation du projet.
