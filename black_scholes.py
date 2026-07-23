"""Black-Scholes pricing and Greek calculations."""

import numpy as np
from scipy.stats import norm


def calculate_d1(S, K, r, sigma, tau):
    """Calculate d1 in the Black-Scholes model."""
    return (
        np.log(S / K)
        + (r + 0.5 * sigma**2) * tau
    ) / (sigma * np.sqrt(tau))


def calculate_d2(S, K, r, sigma, tau):
    """Calculate d2 in the Black-Scholes model."""
    d1 = calculate_d1(S, K, r, sigma, tau)
    return d1 - sigma * np.sqrt(tau)


def call_price(S, K, r, sigma, tau):
    """Calculate the price of a European call option."""
    d1 = calculate_d1(S, K, r, sigma, tau)
    d2 = calculate_d2(S, K, r, sigma, tau)

    return (
        S * norm.cdf(d1)
        - K * np.exp(-r * tau) * norm.cdf(d2)
    )


def call_delta(S, K, r, sigma, tau):
    """Calculate the Delta of a European call option."""
    d1 = calculate_d1(S, K, r, sigma, tau)
    return norm.cdf(d1)


def option_gamma(S, K, r, sigma, tau):
    """Calculate the Gamma of a European call or put option."""
    d1 = calculate_d1(S, K, r, sigma, tau)

    return (
        norm.pdf(d1)
        / (S * sigma * np.sqrt(tau))
    )


def option_vega(S, K, r, sigma, tau):
    """Calculate Vega for a 1.00 change in volatility."""
    d1 = calculate_d1(S, K, r, sigma, tau)
    return S * norm.pdf(d1) * np.sqrt(tau)


def call_theta(S, K, r, sigma, tau):
    """Calculate annualised Theta for a European call option."""
    d1 = calculate_d1(S, K, r, sigma, tau)
    d2 = calculate_d2(S, K, r, sigma, tau)

    time_value_term = (
        -S * norm.pdf(d1) * sigma
        / (2 * np.sqrt(tau))
    )

    discounting_term = (
        -r * K * np.exp(-r * tau) * norm.cdf(d2)
    )

    return time_value_term + discounting_term
