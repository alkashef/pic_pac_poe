import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import Engine, GameServer, GameHelper
from GameServer import app, dummy_engine

game_board = dummy_engine.get_game()
board = pd.DataFrame(game_board.get_board())
p1_name = game_board.get_p1_name()
p2_name = game_board.get_p2_name()
p1_label = game_board.get_p1_label()
p2_label = game_board.get_p2_label()
turn = game_board.get_turn()
first_turn = game_board.get_first_turn()
state = game_board.get_state()


app.layout = html.Div(id='root', children=[
    html.Header(id='game-header', children=[
        html.H1('TIC TAC TOE!')
    ]),
    html.Div(id='game-body', children=[
        html.Div(id='game-state', children=[
            html.H4(GameHelper.get_state(state))
        ]),
        html.Div(id='game-turn', children=[
            html.H4('First Turn' + ": " + GameHelper.get_turn(first_turn)),
            html.H4('Turn' + ": " + GameHelper.get_turn(turn))
        ]),
        html.Div(id='game-players', children=[
            html.H4(p1_name + ": " + GameHelper.get_def(p1_label)),
            html.H4(p2_name + ": " + GameHelper.get_def(p2_label))
        ]),
        html.Div(id='game-board', children=[
            html.Table(GameHelper.to_table(pd.DataFrame(board)))
        ])
    ]),
    dcc.Interval(
            id='interval-component',
            interval=1*4000,
            n_intervals=0
        )
])

if __name__ == '__main__':
    print("in main")
    app.run_server(debug=True)
