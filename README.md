# Jalon 01 : Propre & Structuré

## Objectif
Nettoyer et structurer le jeu de données **E-commerce Data** (Kaggle, carrie1)
avec Pandas, pour que les analyses suivantes reposent sur des données fiables.

## Dataset
- Source : https://www.kaggle.com/datasets/carrie1/ecommerce-data
- Taille brute : 541 909 lignes, 8 colonnes
- Outil : Google Colab (Python, Pandas)

## Étapes réalisées
1. Chargement du fichier (encodage ISO-8859-1)
2. Suppression des doublons exacts
3. Conversion des types : `InvoiceDate` en datetime, `CustomerID` / `InvoiceNo` / `StockCode` en texte
4. Traitement des anomalies métier (voir ci-dessous)
5. Standardisation du texte (Description, StockCode, Country)
6. Ajout de colonnes dérivées : `TotalPrice`, `Year`, `Month`, `YearMonth`
7. Export du fichier nettoyé

## Logique de gestion des retours et anomalies

| Cas détecté | Traitement | Justification |
|---|---|---|
| Facture commençant par `C` avec quantité négative | **Conservé**, marqué `is_return = True` | Ce sont de vrais retours clients. Ils permettent de calculer un taux de retour et un chiffre d'affaires net. |
| Quantité négative SANS facture `C` | **Isolé** dans `anomalies_ecartees.csv` | Ajustements de stock, articles cassés ou perdus : ce ne sont pas des ventes. |
| `UnitPrice` ≤ 0 | **Isolé** dans `anomalies_ecartees.csv` | Ajustements comptables ou dons, sans valeur de vente. |
| StockCode non produit (POST, D, M, BANK CHARGES...) | **Isolé** dans `non_produits_ecartes.csv` | Frais de port, remises et frais bancaires faussent les analyses par produit. |
| `CustomerID` manquant | **Conservé**, colonne `has_customer_id` ajoutée | Ce sont des ventes réelles (clients invités). Les supprimer ferait perdre du chiffre d'affaires. |
| Country = "Unspecified" | Remplacé par valeur manquante | Ce n'est pas un vrai pays. |

Aucune ligne n'est supprimée sans trace : les lignes écartées sont sauvegardées
dans des fichiers séparés.

## Fichiers
- `data/raw_data.csv` : données brutes
- `data/cleaned_data.csv` : données nettoyées
- `data/anomalies_ecartees.csv` : lignes écartées (quantités/prix anormaux)
- `data/non_produits_ecartes.csv` : lignes non-produits écartées
- `notebooks/01_clean_and_structure.ipynb` : notebook de nettoyage

## Résultat
| | Avant | Après |
|---|---|---|
| Lignes | 541 909 | *(à compléter avec votre résultat)* |
| Doublons | *(à compléter)* | 0 |
| Type de InvoiceDate | object | datetime64 |