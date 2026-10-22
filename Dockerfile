# Image Python ultra-légère pour économiser de l'espace disque
FROM python:3.10-slim

# Empêche Python d'écrire des fichiers .pyc et force l'affichage immédiat des logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copie et installation optimisée des dépendances sans conserver le cache pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie des fichiers du projet
COPY . .

# Exposer le port par défaut de Streamlit
EXPOSE 8501

# Commande pour démarrer le tableau de bord
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]