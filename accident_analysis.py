
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("accident_2020.CSV")

# Create output directory
output_dir = "accident_eda_outputs"
os.makedirs(output_dir, exist_ok=True)

# Accidents by State (Top 10)
accidents_by_state = df['STATENAME'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=accidents_by_state.values, y=accidents_by_state.index, palette="rocket")
plt.title("Top 10 States by Number of Accidents (2020)")
plt.xlabel("Number of Accidents")
plt.ylabel("State")
plt.tight_layout()
plt.savefig(f"{output_dir}/accidents_by_state.png")
plt.close()

# Accidents by Light Conditions
light_cond = df['LGT_CONDNAME'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=light_cond.values, y=light_cond.index, palette="coolwarm")
plt.title("Accidents by Light Conditions")
plt.xlabel("Number of Accidents")
plt.ylabel("Light Condition")
plt.tight_layout()
plt.savefig(f"{output_dir}/light_conditions.png")
plt.close()

# Accidents by Weather Conditions
weather_cond = df['WEATHERNAME'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=weather_cond.values, y=weather_cond.index, palette="viridis")
plt.title("Accidents by Weather Conditions")
plt.xlabel("Number of Accidents")
plt.ylabel("Weather Condition")
plt.tight_layout()
plt.savefig(f"{output_dir}/weather_conditions.png")
plt.close()

# Accidents by Hour of the Day
hourly_accidents = df['HOURNAME'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
sns.barplot(x=hourly_accidents.index, y=hourly_accidents.values, palette="magma")
plt.xticks(rotation=45)
plt.title("Accidents by Hour of the Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.savefig(f"{output_dir}/accidents_by_hour.png")
plt.close()
