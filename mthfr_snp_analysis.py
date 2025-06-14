import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("D:/coursera/MTHFR/mthfr_snp_freq.csv")

# Display data to verify
print(df)

# Set seaborn style
sns.set(style="whitegrid")

# Create bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Population", y="Frequency", hue="rsID")

plt.title("MTHFR SNP Frequencies Across Populations")
plt.xlabel("Population Group")
plt.ylabel("Allele Frequency")
plt.legend(title="SNP ID")
plt.tight_layout()

# Save the plot
plt.savefig("mthfr_snp_freq_plot.png", dpi=300)
plt.show()
