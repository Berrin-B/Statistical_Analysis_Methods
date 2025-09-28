"""
descriptive_statistics.py

This file reads student grades from a text file and calculates descriptive
statistics for each assessment: mean, median, standard deviation, and skewness.

Example application for an undergraduate Computational Physics course.
"""

import numpy as np
import math
import os


def load_student_data(filename):
    """
    Load student data from a text file.

    Parameters
    ----------
    filename : str
        Path to the text file.

    Returns
    -------
    dict
        Dictionary containing arrays for each assessment type.
    """
    data = np.loadtxt(filename)
    return {
        "MT1": data[:, 0],
        "MT2": data[:, 1],
        "Final": data[:, 2],
        "Lab": data[:, 3],
        "HW": data[:, 4],
        "Attendance": data[:, 5]
    }


def mean(data):
    """Calculate the mean of a list or array."""
    return sum(data) / len(data)


def median(data):
    """Calculate the median of a list or array."""
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]


def std_deviation(data):
    """Calculate the sample standard deviation."""
    m = mean(data)
    return math.sqrt(sum((x - m) ** 2 for x in data) / (len(data) - 1))


def skewness(data):
    """Calculate the skewness direction (positive or negative)."""
    s = (3 * (mean(data) - median(data))) / std_deviation(data)
    if s > 0:
        return "positive skew"
    elif s < 0:
        return "negative skew"
    else:
        return "symmetric"


if __name__ == "__main__":
    # Safe file path relative to script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "data2.txt")

    grades = load_student_data(filename)

    print("Means of each dataset:")
    for key, values in grades.items():
        print(f"{key}: {mean(values):.2f}")

    print("\nMedians of each dataset:")
    for key, values in grades.items():
        print(f"{key}: {median(values):.2f}")

    print("\nStandard deviations of each dataset:")
    for key, values in grades.items():
        print(f"{key}: {std_deviation(values):.2f}")

    print("\nSkewness direction of each dataset:")
    for key, values in grades.items():
        print(f"{key}: {skewness(values)}")
