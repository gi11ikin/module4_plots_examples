from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, ColorPicker, Button, TextInput, HoverTool
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.server.server import Server

# Initial Data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# Create a ColumnDataSource
source = ColumnDataSource(data=dict(x=x, y=y))

# Create a figure
p = figure(title="Interactive Bokeh Example", x_axis_label='X-axis', y_axis_label='Y-axis')

# Add a circle glyph with tooltips
glyph_circle = p.circle('x', 'y', size=15, color="navy", alpha=0.5, source=source, legend_label="Data Points")
p.line('x', 'y', line_width=2, color="green", alpha=0.5, source=source)

# Add HoverTool for tooltips
hover = HoverTool()
hover.tooltips = [("Index", "$index"), ("(X, Y)", "($x, $y)")]
p.add_tools(hover)

# Callbacks
def update_marker_size(attr, old, new):
    glyph_circle.glyph.size = size_slider.value

def update_line_color(attr, old, new):
    p.line('x', 'y', line_width=2, color=new, alpha=0.5, source=source)

def reset_plot():
    size_slider.value = 15
    color_picker.value = "green"

def add_data_point():
    try:
        new_x = float(x_input.value)
        new_y = float(y_input.value)
        current_data = source.data
        new_x_data = current_data['x'] + [new_x]
        new_y_data = current_data['y'] + [new_y]
        source.data = dict(x=new_x_data, y=new_y_data)
        x_input.value = ""
        y_input.value = ""
    except ValueError:
        pass  # Handle invalid input

# Widgets
size_slider = Slider(title="Marker Size", start=5, end=50, value=15, step=1)
color_picker = ColorPicker(title="Line Color", color="green")
reset_button = Button(label="Reset", button_type="success")
x_input = TextInput(title="New X Value", value="")
y_input = TextInput(title="New Y Value", value="")
add_button = Button(label="Add Data Point", button_type="primary")

# Add widget callbacks
size_slider.on_change('value', update_marker_size)
color_picker.on_change('color', update_line_color)
reset_button.on_click(reset_plot)
add_button.on_click(add_data_point)

# Layout
layout = column(
    p,
    row(size_slider, color_picker, reset_button),
    row(x_input, y_input, add_button)
)

# Modify document
def modify_doc(doc):
    doc.add_root(layout)

# Run Bokeh Server
app = Application(FunctionHandler(modify_doc))

server = Server({'/': app}, port=5006)
server.start()

if __name__ == '__main__':
    print("Opening Bokeh app on http://localhost:5006/")
    server.io_loop.add_callback(server.show, "/")
    server.io_loop.start()
