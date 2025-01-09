# **Jump-Diffusion Model for Apple Stock Price Simulation**

## **Overview**
This repository provides a Python implementation of a **Jump-Diffusion Model** to simulate stock price dynamics with applications in **quantitative finance**. The model combines:
- **Geometric Brownian Motion (GBM)** for continuous price changes.
- **Jump components** modeled by a Poisson process to capture sudden market shocks.

The project provides insights into stochastic modeling of asset prices and offers a starting point for extensions into option pricing, risk management, and other quantitative finance applications.

---



### **Stochastic Process for $$X_t$$**

The model for the stock price dynamics can be written as:

$$
X_t = \mu t + \sigma W_t + \sum_{i=1}^{N_t} Y_i
$$

Where:

- $$X_t$$ is the process representing the evolution of the stock price.
- $$\mu t$$ represents the **drift** (deterministic component).
- $$\sigma W_t$$ is the **continuous part** modeled by **Brownian motion**.
- $$\sum_{i=1}^{N_t} Y_i$$ represents the **discrete jumps**, where:
- $$Y_i$$ is the **size** of the \( i \)-th jump.
- $$N_t$$ is the total number of jumps up to time \( t \), modeled as a **Poisson process**.

This model incorporates both the continuous price fluctuations and the sudden, discrete market jumps.





## **Model Description**

### **Jump-Diffusion Stochastic Process**
The price $S_t$ evolves according to the following equation:

$$dS_t = \mu S_t dt + \sigma S_t dW_t + S_t dJ_t$$

Where:
- $\mu$: Drift rate (expected return).
- $\sigma$: Volatility of continuous price changes.
- $dW_t$: Standard Brownian motion increment.
- $dJ_t$: Jump component governed by a Poisson process.

The jump component $dJ_t$ is defined as:

$$dJ_t = \sum_{i=1}^{N_t} \epsilon_i$$

Here:
- $N_t$: Number of jumps by time $t$, modeled as a Poisson process.
- $\epsilon_i$: Size of the $i$-th jump.

This process captures both the **continuous price movements** and **discrete jumps** observed in financial markets.

---

## **Project Structure**
- **`jump_diffusion_simulation.py`**: Core implementation of the jump-diffusion model.
- **`data/`**: Directory to store historical stock data.
- **`plots/`**: Directory to save generated price simulation graphs.
- **`notebooks/`**: Jupyter notebooks for exploration and visualization.

---

## **Features**
- Fetches historical stock data using Yahoo Finance API.
- Implements a jump-diffusion model for price simulation.
- Visualizes simulated price trajectories over a specified time horizon.
- Parameter tuning for jump intensity, jump size, and volatility.

---

## **Getting Started**

### **Dependencies**
Install the required Python libraries:
```bash
pip install numpy matplotlib pandas yfinance
```

 ## **Usage**

Clone the repository:

```bash
git clone https://github.com/TKoskas/Apple-Stock-Jump-Diffusion.git
cd Apple-Stock-Jump-Diffusion
```

Run the Python script:

```bash
python jump_diffusion_simulation.py
```

Customize parameters in the script:

`lambda_jump`: Jump intensity.
`mu_jump`: Mean jump size.
`sigma_jump`: Volatility of jump sizes.

View the output plot of simulated stock prices.

## **Applications**
This model can be extended for:

Option pricing: Use Merton's jump-diffusion model to price options.

Risk management: Simulate worst-case scenarios from sudden market shocks.

Portfolio optimization: Incorporate jump risks into portfolio construction.

## **Acknowledgments**
This project was inspired by classic quantitative finance texts and stochastic modeling principles, including:

Merton's Jump-Diffusion Model

Credit Risk Modeling: Theory and Applications by David Lando
## **License**
This project is licensed under the MIT License.
