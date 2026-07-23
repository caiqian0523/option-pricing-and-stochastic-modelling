# Option Pricing and Stochastic Modelling

A Python project exploring geometric Brownian motion, Monte Carlo option
pricing and Black–Scholes risk sensitivities.

## Contents

### 1. Geometric Brownian Motion Simulation

- Simulates vectorised GBM price paths
- Implements the exact solution with the Itô correction term
- Compares the simulated terminal mean with its theoretical value

### 2. Monte Carlo Option Pricing

- Prices European call options under the risk-neutral measure
- Compares Monte Carlo estimates with the Black–Scholes formula
- Studies convergence as the number of simulations increases
- Calculates standard errors and 95% confidence intervals

### 3. Black–Scholes Greeks

- Implements analytical Delta, Gamma, Vega and Theta
- Visualises each Greek across underlying prices
- Identifies the exact Gamma and Vega peak locations
- Validates analytical Greeks using central finite differences
- Examines truncation and floating-point errors across step sizes

## Methods

- Geometric Brownian motion
- Risk-neutral pricing
- Monte Carlo simulation
- Black–Scholes model
- Option Greeks
- Central finite differences
- Convergence and numerical error analysis

## Technologies

- Python
- NumPy
- Matplotlib
- SciPy
- Jupyter Notebook

## Notebooks

- `01_gbm_simulation.ipynb`
- `02_monte_carlo_option_pricing.ipynb`
- `03_black_scholes_greeks.ipynb`
