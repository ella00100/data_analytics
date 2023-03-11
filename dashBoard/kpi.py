import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import pandas as pd

app = dash.Dash("K-Index",
                external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'KOSPI', 'value': './data/kospi.xlsx'},
            {'label': 'KOSPI200', 'value': './data/kpi200.xlsx'},
            {'label': 'KOSDAQ', 'value': './data/kosdaq.xlsx'}
        ],
        value='./data/kospi.xlsx'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '600'})

# app layout-> html 수정
app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])

def update_graph(selected_dropdown_value):
    df = pd.read_excel(selected_dropdown_value).sort_values(by="date")
    return {
        'data': [
            {'x': df.date,
             'y': df.price}
        ],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

app.run_server(debug=True, use_reloader=False)