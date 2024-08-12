import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

# Initialize the Dash app
app = dash.Dash(__name__)

# Initial Data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# Layout of the app
app.layout = html.Div([
    dcc.Graph(id='graph'),
    html.Div([
        html.Label('Marker Size'),
        dcc.Slider(id='size-slider', min=5, max=50, step=1, value=15),
        html.Label('Line Color'),
        dcc.Dropdown(
            id='color-picker',
            options=[
                {'label': 'Green', 'value': 'green'},
                {'label': 'Red', 'value': 'red'},
                {'label': 'Blue', 'value': 'blue'},
                {'label': 'Orange', 'value': 'orange'},
                {'label': 'Purple', 'value': 'purple'}
            ],
            value='green'
        ),
        html.Label('New X Value'),
        dcc.Input(id='x-input', type='number', value=''),
        html.Label('New Y Value'),
        dcc.Input(id='y-input', type='number', value=''),
        html.Button('Add Data Point', id='add-button', n_clicks=0),
        html.Button('Reset', id='reset-button', n_clicks=0),
    ]),
])

@app.callback(
    Output('graph', 'figure'),
    Input('size-slider', 'value'),
    Input('color-picker', 'value'),
    Input('add-button', 'n_clicks'),
    Input('reset-button', 'n_clicks'),
    State('x-input', 'value'),
    State('y-input', 'value')
)
def update_graph(size, color, add_n_clicks, reset_n_clicks, new_x, new_y):
    global x, y

    # Handle the Reset Button Click
    if reset_n_clicks > 0:
        x = [1, 2, 3, 4, 5]
        y = [6, 7, 2, 4, 5]
    
    # Handle the Add Data Point Button Click
    if add_n_clicks > 0 and new_x and new_y:
        try:
            x.append(float(new_x))
            y.append(float(new_y))
        except ValueError:
            pass  # Handle invalid input
    
    # Create the plot
    trace1 = go.Scatter(
        x=x,
        y=y,
        mode='markers+lines',
        marker=dict(size=size, color='navy', opacity=0.5),
        line=dict(width=2, color=color),
        text=[f'({xi}, {yi})' for xi, yi in zip(x, y)],
        hoverinfo='text'
    )
    
    layout = go.Layout(
        title='Interactive Plot',
        xaxis=dict(title='X-axis'),
        yaxis=dict(title='Y-axis')
    )
    
    return {'data': [trace1], 'layout': layout}

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
