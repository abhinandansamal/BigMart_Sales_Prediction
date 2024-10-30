# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_distributions(df, columns):
    """
    Plots distributions for specified columns.
    """
    for column in columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[column])
        plt.title(f"Distribution of {column}")
        plt.show()