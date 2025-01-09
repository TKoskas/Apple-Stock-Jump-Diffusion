import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

# Télécharger les données historiques d'Apple
ticker = 'AAPL'
data = yf.download(ticker, start="2010-01-01", end="2025-01-01")

# Vérification des colonnes disponibles
print("Colonnes disponibles :", data.columns)

# Utilisation de 'Adj Close' si disponible, sinon 'Close'
if 'Adj Close' in data.columns:
    data['Log Ret'] = np.log(data['Adj Close'] / data['Adj Close'].shift(1))
else:
    print("'Adj Close' non disponible, utilisation de 'Close' à la place.")
    data['Log Ret'] = np.log(data['Close'] / data['Close'].shift(1))

# Paramètres du modèle
T = 1.0         # Horizon temporel (1 an)
N = 252         # Nombre de jours de trading par an
dt = T / N      # Incrément de temps (1 jour de trading)
lambda_jump = 0.05  # Intensité des sauts
mu_jump = 0      # Moyenne des sauts
sigma_jump = 0.01  # Écart-type des sauts

# Calculer la volatilité historique (en utilisant les rendements log)
sigma = data['Log Ret'].std()

# Simuler le mouvement brownien et les sauts
time = np.linspace(0, T, N)  # Ajuster le nombre de points à 252
dW = np.random.normal(0, np.sqrt(dt), N)  # Incréments du mouvement brownien
W = np.cumsum(dW)  # Chemin du processus brownien

# Simuler les sauts
jump_count = np.random.poisson(lambda_jump * dt, N)  # Nombre de sauts à chaque étape
jump_sizes = np.random.normal(mu_jump, sigma_jump, N)  # Taille des sauts
jumps = jump_count * jump_sizes  # Amplitude des sauts

# Simuler l'évolution du prix avec le modèle jump-diffusion
S0 = data['Close', 'AAPL'].iloc[-1]  # Dernier prix de l'action d'Apple
X = S0 * np.exp(np.cumsum(dW) + np.cumsum(jumps))  # Modèle jump-diffusion

# Tracer l'évolution du prix simulé
plt.figure(figsize=(12, 6))
plt.plot(time, X, label="Évolution simulée du prix")
plt.title(f"Simulation du prix d'Apple pour 2025 avec modèle Jump-Diffusion")
plt.xlabel("Temps (en années)")
plt.ylabel("Prix de l'action (simulé)")
plt.legend()
plt.show()