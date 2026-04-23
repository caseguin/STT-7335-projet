# STT-7335 — Projet : Prédiction de volatilité sur cryptomonnaies

Prédiction binaire de volatilité sur des données OHLCV à la minute (BTC, ETH, SOL, SUI) à l'aide de modèles de machine learning.

## Données

Données OHLCV 1-minute disponibles sur [cryptoarchive.com.au](https://www.cryptoarchive.com.au/).

Placer les fichiers suivants à la racine du projet :
- `BTCUSDT.csv`
- `ETHUSDT.csv`
- `SOLUSDT.csv`
- `SUIUSDT.csv`


## Utilisation

Ouvrir et exécuter `projet.ipynb` de haut en bas.

## Structure du notebook

1. Chargement des données
2. Feature engineering et construction de la cible
3. Analyse exploratoire
4. Entraînement et évaluation des modèles (walk-forward CV)
5. Généralisation sur ETH, SOL, SUI
