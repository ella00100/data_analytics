import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import pandas as pd

# dashboard app
app = dash.Dash('Naver Shopping Trend',
                external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

# app layout-> html 수정.
app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            # dropdown 메뉴 만들기!
            {'label': 'Apple', 'value': './naver_shopping(애플).xlsx'},
            {'label': 'Samsung', 'value': './naver_shopping(삼성전자).xlsx'},
            {'label': 'Xiaomi', 'value': './naver_shopping(샤오미).xlsx'}
        ],
        value='./naver_shopping(애플).xlsx'  # 기본값 세팅하기
    ),
    dcc.Graph(id='my-graph')
], style={'width': '600'})


@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
# dash가 실제로 실행하는 그래프를 update_graph 함수로 정의합니다.
def update_graph(selected_dropdown_value):
    # 내가 선택한 label에 해당하는 파일 이름
    df = pd.read_excel(selected_dropdown_value)
    return {
        'data': [
            # dash가 보여줄 dashboard의 그래프를 dict 형태로 지정합니다.
            {'x': df.index,
             'y': df["리뷰수"]}

        ],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }


# dash app이 실행됩니다.
# app.run_server(debug=True, use_reloader=False)
app.run_server(host='192.168.56.1', port=3003)