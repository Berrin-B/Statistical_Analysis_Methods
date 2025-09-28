"""
exponential_clt_simulation.py

This file demonstrates the Central Limit Theorem using the exponential distribution.
It simulates the means of samples of different sizes and plots histograms.

Example application for an undergraduate Computational Physics course.
"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_exponential_means(sample_sizes, num_simulations=1000, random_seed=None):
    """
    Simulate the means of exponential random variables for different sample sizes.

    Parameters
    ----------
    sample_sizes : list of int
        List of sample sizes (n values) to simulate.
    num_simulations : int, optional
        Number of repetitions for each sample size (default is 1000).
    random_seed : int, optional
        Random seed for reproducibility (default is None).

    Returns
    -------
    list of ndarray
        A list where each element is an array of means for a given sample size.
    """
    if random_seed is not None:
        np.random.seed(random_seed)

    all_means = []
    for n in sample_sizes:
        means = []
        for _ in range(num_simulations):
            sample = np.random.exponential(size=n)
            means.append(np.mean(sample))
        all_means.append(np.array(means))
    return all_means


if __name__ == "__main__":
    # Parameters
    sample_sizes = [1, 2, 5, 10, 20, 50]
    num_simulations = 1000

    # Simulate means
    mean_values = simulate_exponential_means(sample_sizes, num_simulations)

    # Plotting
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    axes = axes.flatten()

    for i, n in enumerate(sample_sizes):
        axes[i].hist(mean_values[i], bins=100, alpha=0.7, color='skyblue')
        axes[i].set_title(f"Sample size n = {n}")
        axes[i].set_xlabel("Mean")
        axes[i].set_ylabel("Frequency")

    plt.tight_layout()
    plt.show()
