import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV dataset
df = pd.read_csv("sales_data.csv")

# Display dataset
print("Dataset:")
print(df)

# Statistics Summary
print("\nStatistics Summary:")
print(df.describe())

# -------------------------
# Bar Chart
# -------------------------
plt.figure(figsize=(6,4))

df.groupby("Category")["Sales"].sum().plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("bar_chart.png")
plt.close()

# -------------------------
# Histogram
# -------------------------
plt.figure(figsize=(6,4))

plt.hist(df["Sales"], bins=5, edgecolor="black")

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("histogram.png")
plt.close()

# -------------------------
# Correlation Heatmap
# -------------------------
plt.figure(figsize=(6,4))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="Blues"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("correlation.png")
plt.close()

print("\nEDA Completed Successfully")
print("Charts Saved Successfully")