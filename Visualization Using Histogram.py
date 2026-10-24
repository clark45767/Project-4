
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the Penguins dataset
url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
df = pd.read_csv(url)

# Define the features, bin ranges, bin widths, and colors
features = [
    ("bill_length_mm", "Culmen Length (mm)", 30, 60, 3, "skyblue"),
    ("bill_depth_mm", "Culmen Depth (mm)", 12, 22, 1, "salmon"),
    ("flipper_length_mm", "Flipper Length (mm)", 170, 235, 5, "lightgreen"),
    ("body_mass_g", "Body Mass (g)", 2500, 6500, 250, "orange")
]

# Create four histograms
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for ax, (column, title, start, end, width, color) in zip(axes, features):
    data = df[column].dropna()
    bins = np.arange(start, end + width, width)

    ax.hist(data, bins=bins, color=color, edgecolor="black")
    ax.set_title(title)
    ax.set_xlabel(title)
    ax.set_ylabel("Frequency")
    ax.set_xticks(bins[::max(1, len(bins) // 8)])
    ax.grid(axis="y", alpha=0.3)

plt.suptitle("Histograms of Penguin Measurements", fontsize=16)
plt.tight_layout()
plt.show()
