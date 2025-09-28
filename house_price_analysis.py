"""
house_price_analysis.py

This file analyzes house selling price data, calculating mean, standard deviation,
margin of error, 95% confidence interval, and plots a histogram of selling prices.

Example application for an undergraduate Computational Physics course.
"""

import numpy as np
import matplotlib.pyplot as plt
import os


def load_house_data(filename):
    """
    Load house data from a text file.

    Parameters
    ----------
    filename : str
        Path to the text file. Assumes at least three columns: [id, price, size]

    Returns
    -------
    tuple of arrays
        Selling prices and house sizes.
    """
    data = np.loadtxt(filename)
    selling_prices = data[:, 1]
    house_sizes = data[:, 2]
    return selling_prices, house_sizes


def mean(data):
    """Calculate mean."""
    return sum(data) / len(data)


def std_deviation(data):
    """Calculate standard deviation."""
    m = mean(data)
    return np.sqrt(sum((x - m) ** 2 for x in data) / len(data))


def confidence_interval(data, z=1.96):
    """Calculate margin of error for 95% confidence interval."""
    return z * std_deviation(data) / np.sqrt(len(data))


if __name__ == "__main__":
    # Safe path relative to script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "data.txt")

    selling_prices, house_sizes = load_house_data(filename)

    # Average selling price per m^2
    price_per_m2 = selling_prices / house_sizes
    avg_price_per_m2 = mean(price_per_m2)
    avg_price_adjusted = avg_price_per_m2 * mean(house_sizes)

    # Statistics
    mean_price = mean(selling_prices)
    margin_error = confidence_interval(selling_prices)
    conf_low = mean_price - margin_error
    conf_high = mean_price + margin_error

    # Print results
    print(f"Average selling price (raw): {mean_price:.2f}")
    print(f"Average selling price using price/house size: {avg_price_adjusted:.2f}")
    print(f"Margin of error: {margin_error:.2f}")
    print(f"95% Confidence interval: {conf_low:.2f} < μ < {conf_high:.2f}")

    # Plot histogram
    plt.hist(selling_prices, bins=10, alpha=0.7, color="skyblue")
    plt.title("Histogram of Selling Prices")
    plt.xlabel("Selling price")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()
