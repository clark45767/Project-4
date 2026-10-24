
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Penguins dataset
url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
df = pd.read_csv(url)

# Select numerical features
features = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g"
]

# Remove rows with missing values
df = df.dropna(subset=features)

# 1. Scatter plot: Culmen Length vs Body Mass
plt.figure(figsize=(8, 5))
plt.scatter(df["bill_length_mm"], df["body_mass_g"], color="blue")
plt.title("Culmen Length vs Body Mass")
plt.xlabel("Culmen Length (mm)")
plt.ylabel("Body Mass (g)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 2. Scatter plot: Culmen Depth vs Body Mass
plt.figure(figsize=(8, 5))
plt.scatter(df["bill_depth_mm"], df["body_mass_g"], color="red")
plt.title("Culmen Depth vs Body Mass")
plt.xlabel("Culmen Depth (mm)")
plt.ylabel("Body Mass (g)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 3. Pair plot: Relationships between all numerical features
sns.pairplot(df, vars=features, hue="species")
plt.suptitle("Pair Plot of Penguin Measurements", y=1.02)
plt.show()

# 4. Area graph: Culmen Length vs Body Mass
# Sort by culmen length to make the area graph easier to read
area_df = df.sort_values("bill_length_mm")

plt.figure(figsize=(8, 5))
plt.fill_between(
    area_df["bill_length_mm"],
    area_df["body_mass_g"],
    color="lightgreen",
    alpha=0.7
)
plt.plot(
    area_df["bill_length_mm"],
    area_df["body_mass_g"],
    color="green"
)
plt.title("Area Graph: Culmen Length vs Body Mass")
plt.xlabel("Culmen Length (mm)")
plt.ylabel("Body Mass (g)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
