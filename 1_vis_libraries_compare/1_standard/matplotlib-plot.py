import matplotlib.pyplot as plt

# Create a figure
plt.figure()

# Plot data
plt.plot([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], marker='o', color='red')

# Customize the plot
plt.title("Matplotlib Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Save the plot
plt.savefig("./1_vis_libraries_compare/1_standard/data/matplotlib_plot.png")



