"""Tests for the Black-Scholes module."""

import numpy as np

from black_scholes import (
    call_delta,
    call_price,
    call_theta,
    option_gamma,
    option_vega,
)


S = 100
K = 100
R = 0.05
SIGMA = 0.20
TAU = 1


def test_call_price():
    result = call_price(S, K, R, SIGMA, TAU)
    assert np.isclose(result, 10.45058357, atol=1e-8)


def test_call_delta():
    result = call_delta(S, K, R, SIGMA, TAU)
    assert np.isclose(result, 0.63683065, atol=1e-8)


def test_option_gamma():
    result = option_gamma(S, K, R, SIGMA, TAU)
    assert np.isclose(result, 0.01876202, atol=1e-8)


def test_option_vega():
    result = option_vega(S, K, R, SIGMA, TAU)
    assert np.isclose(result, 37.52403469, atol=1e-8)


def test_call_theta():
    result = call_theta(S, K, R, SIGMA, TAU)
    assert np.isclose(result, -6.41402755, atol=1e-8)
