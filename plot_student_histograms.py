"""
plot_student_histograms.py

This file loads student grade data from a text file and plots histograms
for each assessment type, fitting a normal distribution to the first midterm (MT1).

Example application for an undergraduate Computational Physics course.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def plot_histograms(filename):
    """
    Load student data from a file and plot histograms for each assessment.

    Parameters
    ----------
    filename : str
        Path to the text file containing student data.

    Returns
    -------
    None
    """
    # Load data from the text file
    data = np.loadtxt(filename)

    # Separate columns into individual lists
    mt1 = data[:, 0]
    mt2 = data[:, 1]
    final_exam = data[:, 2]
    lab = data[:, 3]
    homework = data[:, 4]
    attendance = data[:, 5]

    # Set up 2x3 subplot figure
    fig, axes = plt.subplots(2, 3, figsize=(12, 6))
    fig.tight_layout(pad=3.0)

    # MT1 histogram with normal distribution fit
    ax = axes[0, 0]
    n, bins, _ = ax.hist(mt1, bins=10, density=True, alpha=0.5)
    mu, sigma = stats.norm.fit(mt1)
    best_fit_line = stats.norm.pdf(bins, mu, sigma)
    ax.plot(bins, best_fit_line, "r--")
    ax.set_title("MT1")

    # Other histograms
    axes[0, 1].hist(mt2, bins=10)
    axes[0, 1].set_title("MT2")

    axes[0, 2].hist(final_exam, bins=10)
    axes[0, 2].set_title("Final Exam")

    axes[1, 0].hist(lab, bins=10)
    axes[1, 0].set_title("Lab")

    axes[1, 1].hist(homework, bins=10)
    axes[1, 1].set_title("Homework")

    axes[1, 2].hist(attendance, bins=10)
    axes[1, 2].set_title("Attendance")

    # Show the figure
    plt.show()


if __name__ == "__main__":
    filename = r"Desktop\data_science_projects\computational_methods_updated\statistical_analysis_methods\data2.txt"  # Path to your data file
    plot_histograms(filename)
