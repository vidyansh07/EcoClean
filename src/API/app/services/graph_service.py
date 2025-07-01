import json
import os
import pygal
from pygal.style import Style
from enum import Enum
from datetime import datetime

class graph_types(Enum):
    Line:str = "Line"
    Bar:str = "Bar"


def time_formater(timestamp: int):
    return datetime.fromtimestamp(timestamp).strftime('%d %b, %Y %H:%M:%S')

def generate_graph(Data , graph_type:graph_types = 'Line', BASE_PATH = "."):    

    custom_style = Style(
            colors=('#0343df', '#e50000', '#ffff14', '#929591'),
            font_family='Roboto,Helvetica,Arial,sans-serif',
            background='transparent',
            label_font_size=11,
        )
    if graph_type.value in pygal.CHARTS_BY_NAME.keys():
        graph_function : pygal.Graph = eval(f"pygal.{graph_type.value}")
    else :
        graph_function: pygal.Graph = pygal.Line

    c = graph_function(
            title="Carbon monoxide Data",
            style=custom_style,
            y_title='CO level',
            width=1200,
            x_label_rotation=315,
        )


    data = json.loads(Data)

    c.add('CO', [x['sensor_values']['CO_PPM'] for x in data['Results']])
    c.x_labels = [time_formater(x['timestamp']) for x in data['Results']]
    data= c.render_data_uri()
    return data
    