"""
linear_regression_anova.py

This script performs simple linear regression on two variables (mt1 and mt2)
and calculates regression statistics including SSR, SSE, MSR, MSE, F-statistic, and R^2.
It also plots the data and the regression line.

Example application for an undergraduate Computational Physics course.
"""

import numpy as np
import matplotlib.pyplot as plt


def linear_regression_analysis(x, y):
    """
    Perform linear regression and calculate statistics.

    Parameters
    ----------
    x : array_like
        Independent variable.
    y : array_like
        Dependent variable.

    Returns
    -------
    alpha : float
        Intercept of regression line.
    beta : float
        Slope of regression line.
    r2 : float
        Coefficient of determination.
    stats : dict
        Dictionary containing regression statistics (SSR, SSE, MSR, MSE, F).
    """
    x = np.array(x)
    y = np.array(y)
    n = len(x)

    # Regression coefficients
    beta = (np.sum(x * y) - np.sum(x) * np.sum(y) / n) / (np.sum(x ** 2) - (np.sum(x) ** 2) / n)
    alpha = np.mean(y) - beta * np.mean(x)

    # Sum of squares
    s_xy = np.sum(x * y) - np.sum(x) * np.sum(y) / n
    s_xx = np.sum(x ** 2) - (np.sum(x) ** 2) / n
    s_yy = np.sum(y ** 2) - (np.sum(y) ** 2) / n
    ssr = s_xy ** 2 / s_xx
    sse = s_yy - ssr
    msr = ssr  # Since regression df = 1
    mse = sse / (n - 2)
    f_stat = msr / mse
    r2 = ssr / s_yy

    stats = {
        "Regression": [1, ssr, msr, f_stat],
        "Error": [n - 2, sse, mse, ""],
        "Total": [n - 1, s_yy, "", ""]
    }

    return alpha, beta, r2, stats


if __name__ == "__main__":
    # Load data
    data = np.loadtxt(r"Desktop\data_science_projects\computational_methods_updated\statistical_analysis_methods\data2.txt")
    mt1 = data[:, 0]
    mt2 = data[:, 1]

    # Perform regression
    alpha, beta, r2, stats = linear_regression_analysis(mt1, mt2)

    # Print ANOVA table
    print("{:<10} {:<10} {:<10} {:<10} {:<10}".format("Source", "df", "SS", "MS", "F"))
    for source, values in stats.items():
        df, ss, ms, f_val = values
        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(source, float(df), float(ss), ms, f_val))

    print(f"R^2 = {r2:.4f}")

    # Plot
    plt.scatter(mt1, mt2, label="Data")
    plt.plot(mt1, alpha + beta * mt1, color="red", label="Regression line")
    plt.xlabel("MT1")
    plt.ylabel("MT2")
    plt.title("Linear Regression Analysis")
    plt.legend()
    plt.grid(True)
    plt.show()
