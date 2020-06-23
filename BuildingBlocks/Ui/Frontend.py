import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd

import Engine

external_stylesheets = [__name__, 'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(external_stylesheets=external_stylesheets)

dummy_engine = Engine.Engine()
game_board = dummy_engine.start_game()
board = pd.DataFrame(game_board.get_board())
p1_name = game_board.get_p1_name()
p2_name = game_board.get_p2_name()
p1_label = game_board.get_p1_label()
p2_label = game_board.get_p2_label()
turn = game_board.get_turn()
first_turn = game_board.get_first_turn()
state = game_board.get_state()


def to_table(dataframe):
    rows = []
    for i in range(len(dataframe)):
        row = []
        for col in dataframe.columns:
            value = dataframe.iloc[i][col]
            cell = html.Td(children=value)
            row.append(cell)
        rows.append(html.Tr(row))
    return html.Table(
        rows
    )


app.layout = html.Div(children=[
    html.H1(children="Welcome to Pic Pac Poe!"),
    to_table(board)
])

if __name__ == '__main__':
    print("in main")
    app.run_server(debug=True)
