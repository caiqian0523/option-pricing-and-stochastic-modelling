# Option Pricing and Stochastic Modelling

A Python project exploring geometric Brownian motion and Monte Carlo
pricing of European call options.

## Contents

### 1. Geometric Brownian Motion Simulation

- Simulates vectorised GBM price paths
- Implements the exact GBM solution with the Itô correction term
- Compares the simulated terminal mean with its theoretical value

### 2. Monte Carlo Option Pricing

- Prices European call options under the risk-neutral measure
- Compares Monte Carlo estimates with the Black–Scholes formula
- Studies convergence as the number of simulations increases
- Calculates standard errors and 95% confidence intervals

## Methods

- Geometric Brownian motion
- Risk-neutral pricing
- Monte Carlo simulation
- Black–Scholes model
- Convergence and error analysis

## Technologies

- Python
- NumPy
- Matplotlib
- SciPy

## Notebooks

- `01_gbm_simulation.ipynb`
- `02_monte_carlo_option_pricing.ipynb`
