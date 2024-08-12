import dash
from dash import dcc, html
import plotly.graph_objs as go

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the figure using Plotly
fig = go.Figure()

# Add a scatter plot
fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5], y=[6, 7, 2, 4, 5],
                         mode='markers+lines',
                         marker=dict(color='green', size=10)))

# Customize the layout
fig.update_layout(title="Dash Example", xaxis_title="X-axis", yaxis_title="Y-axis")

# Define the layout of the Dash app
app.layout = html.Div([
    html.H1("Dash Example"),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
