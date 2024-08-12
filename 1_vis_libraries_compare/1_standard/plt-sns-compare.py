import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Matplotlib sample data
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 8, 27, 64, 125]
y3 = [2, 5, 10, 17, 26]

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Plot each data series with different colors and markers
plt.plot(x, y1, marker='o', color='blue', label='y = x^2')
plt.plot(x, y2, marker='s', color='green', label='y = x^3')
plt.plot(x, y3, marker='^', color='red', label='y = 2x + 1')

# Add a title, axis labels, grid, and legend
plt.title("Matplotlib: Multiple Categories")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()

# Save the figure
plt.savefig("./1_vis_libraries_compare/1_standard/data/matplotlib_complex_plot.png")

# Seaborn sample data
data = {
    'x': [1, 2, 3, 4, 5] * 3,
    'y': [1, 4, 9, 16, 25, 1, 8, 27, 64, 125, 2, 5, 10, 17, 26],
    'Category': ['y = x^2'] * 5 + ['y = x^3'] * 5 + ['y = 2x + 1'] * 5
}

# Convert to dataframe
df = pd.DataFrame(data)

# Set the theme and style
sns.set(style="darkgrid")

# Create the plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='x', y='y', hue='Category', style='Category', markers=True, data=df, palette='deep')

# Add a title and axis labels
plt.title("Seaborn: Multiple Categories")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Save the plot
plt.savefig("./1_vis_libraries_compare/1_standard/data/seaborn_complex_plot.png")
