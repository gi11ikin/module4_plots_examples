import seaborn as sns
import matplotlib.pyplot as plt

# Create a figure
plt.figure()

# Plot data using Seaborn
sns.lineplot(x=[1, 2, 3, 4, 5], y=[6, 7, 2, 4, 5], marker='o', color='purple')

# Customize the plot
plt.title("Seaborn Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Save the plot
plt.savefig('./1_vis_libraries_compare/1_standard/data/seaborn_example.png')


