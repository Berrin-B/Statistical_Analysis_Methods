"""
poisson_distribution.py

This file demonstrates analyzing discrete event data using the Poisson distribution.
It calculates the expected counts, fits a Poisson distribution, and plots the results.

Example application for an undergraduate Computational Physics course.
"""

import numpy as np
import matplotlib.pyplot as plt
from math import factorial, exp


def poisson_analysis(events, intervals):
    """
    Analyze data using the Poisson distribution.

    Parameters
    ----------
    events : list of int
        List of discrete number of events (k values).
    intervals : list of int
        Number of intervals corresponding to each event count.

    Returns
    -------
    expected_counts : list of float
        Expected counts according to Poisson distribution.
    alpha : float
        Mean of the Poisson distribution.
    """
    # Calculate the mean (alpha)
    total_events = sum(k * n for k, n in zip(events, intervals))
    total_intervals = sum(intervals)
    alpha = total_events / total_intervals

    # Compute expected counts using Poisson formula
    expected_counts = [
        (alpha**k * exp(-alpha) / factorial(k)) * total_intervals
        for k in events
    ]

    return expected_counts, alpha


if __name__ == "__main__":
    # Data
    no_events = list(range(10))
    no_intervals = [1042, 860, 307, 78, 15, 3, 0, 0, 0, 1]

    expected_counts, alpha = poisson_analysis(no_events, no_intervals)

    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Linear scale
    axes[0].bar(no_events, no_intervals, alpha=0.5, label="Data")
    axes[0].plot(no_events, expected_counts, "ro", label="Poisson fit")
    axes[0].set_xlabel("Number of events")
    axes[0].set_ylabel("Number of intervals")
    axes[0].set_title("Poisson Distribution (Linear Scale)")
    axes[0].legend()

    # Logarithmic scale
    axes[1].bar(no_events, no_intervals, alpha=0.5, label="Data")
    axes[1].plot(no_events, expected_counts, "ro", label="Poisson fit")
    axes[1].set_yscale("log")
    axes[1].set_xlabel("Number of events")
    axes[1].set_ylabel("Number of intervals")
    axes[1].set_title("Poisson Distribution (Log Scale)")
    axes[1].legend()

    plt.tight_layout()
    plt.show()

    print(f"Mean (alpha) of Poisson distribution: {alpha:.4f}")
    print("Expected counts:", expected_counts)
