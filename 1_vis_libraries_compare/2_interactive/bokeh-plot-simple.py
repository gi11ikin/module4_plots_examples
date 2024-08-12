from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.models import Button
from bokeh.io import show, output_file, save
from bokeh.server.server import Server
from bokeh.embed import server_document
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler

# Data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# Create a ColumnDataSource
source = ColumnDataSource(data=dict(x=x, y=y))

# Create a figure
p = figure(title="Bokeh Example", x_axis_label='X-axis', y_axis_label='Y-axis')

# Add a circle glyph
p.circle('x', 'y', size=15, color="navy", alpha=0.5, source=source)
p.line('x', 'y', line_width=2, color="green", alpha=0.5, source=source)

# Set up layouts and add to document
layout = column(p)

def modify_doc(doc):
    doc.add_root(layout)

# Running the Bokeh Server
app = Application(FunctionHandler(modify_doc))

server = Server({'/': app}, port=5006)
server.start()

if __name__ == '__main__':
    print("Opening Bokeh app on http://localhost:5006/")
    server.io_loop.add_callback(server.show, "/")
    server.io_loop.start()
