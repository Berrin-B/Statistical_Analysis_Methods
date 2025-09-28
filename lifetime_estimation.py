"""
lifetime_estimation.py

This script estimates the lifetime of a decay process using weighted linear regression.
It calculates the lifetime, its uncertainty, chi-square, and probability, and plots the fit.

Example application for an undergraduate Computational Physics course.
"""

import numpy as np
import matplotlib.pyplot as plt


def estimate_lifetime(t, N_i, y):
    """
    Estimate the lifetime using weighted linear regression.

    Parameters
    ----------
    t : array_like
        Time data points.
    N_i : array_like
        Number of observed events (used for chi-square calculation).
    y : array_like
        Dependent variable (e.g., log-transformed counts).

    Returns
    -------
    lifetime : float
        Estimated lifetime.
    lifetime_error : float
        Uncertainty in lifetime.
    chi_square : float
        Chi-square of the fit.
    probability : float
        Reduced chi-square (chi-square / degrees of freedom).
    alpha, beta : float
        Fit parameters for linear model y = alpha + beta*t.
    """
    t = np.array(t)
    y = np.array(y)
    N_i = np.array(N_i)
    n = len(t)

    m = np.mean(y)
    s = ((y - m) ** 2) / n

    # Weighted linear regression formulas
    S = np.sum(1 / s)
    St = np.sum(t / s)
    Sy = np.sum(y / s)
    Stt = np.sum(t ** 2 / s)
    Sty = np.sum(t * y / s)

    denominator = S * Stt - St ** 2
    alpha = (Sy * Stt - St * Sty) / denominator
    beta = (S * Sty - St * Sy) / denominator

    lifetime = -1 / beta
    s_b = S / denominator
    lifetime_error = np.sqrt(s_b) / (beta ** 2)

    # Chi-square
    expected_N = np.exp(alpha) * np.exp(-t / lifetime)
    chi_square = np.sum((N_i - expected_N) ** 2 / expected_N)
    dof = n - 2
    probability = chi_square / dof

    return lifetime, lifetime_error, chi_square, probability, alpha, beta


if __name__ == "__main__":
    # Data
    t = np.array([0, 15, 30, 45, 60, 75, 90, 105, 120, 135])
    N_i = [106, 80, 98, 75, 74, 73, 49, 38, 37, 22]
    y = np.array([4.663, 4.382, 4.585, 4.317, 4.304, 4.290, 3.892, 3.638, 3.611, 3.091])

    lifetime, lifetime_error, chi_square, prob, alpha, beta = estimate_lifetime(t, N_i, y)

    # Plot fit
    plt.scatter(t, y, label="Data")
    plt.plot(t, alpha + beta * t, color="red", label="Weighted linear fit")
    plt.xlabel("Time")
    plt.ylabel("y")
    plt.title("Lifetime Estimation via Weighted Linear Regression")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print results
    print(f"Lifetime = {lifetime:.3f} ± {lifetime_error:.3f}")
    print(f"Chi-square: {chi_square:.3f}")
    print(f"Reduced chi-square (probability): {prob:.3f}")
