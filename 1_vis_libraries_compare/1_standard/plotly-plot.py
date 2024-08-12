import plotly.graph_objs as go

# Create a figure
fig = go.Figure()

# Add a scatter plot
fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5], y=[6, 7, 2, 4, 5],
                         mode='markers+lines',
                         marker=dict(color='green', size=10)))

# Customize the layout
fig.update_layout(title="Plotly Example", xaxis_title="X-axis", yaxis_title="Y-axis")

# Save the plot
fig.write_image("./1_vis_libraries_compare/1_standard/data/plotly_plot.png")


