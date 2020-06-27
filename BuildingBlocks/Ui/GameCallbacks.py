import GameServer
from GameServer import app, dummy_engine, turns, states, defs
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import pandas as pd


game_board = dummy_engine.get_game()
board = pd.DataFrame(game_board.get_board())
board = pd.DataFrame(game_board.get_board())
p1_name = game_board.get_p1_name()
p2_name = game_board.get_p2_name()
p1_label = game_board.get_p1_label()
p2_label = game_board.get_p2_label()
turn = game_board.get_turn()
first_turn = game_board.get_first_turn()
state = game_board.get_state()


@app.callback(Output('game-body', 'children'), [Input('cell-'+str(i)+'-'+str(j), "n_clicks") for i in range(len(
                                        pd.DataFrame(board))) for j in range(len(pd.DataFrame(board)))]
                                            + [Input('interval-component', 'n_intervals')])
def func(*args):
    ctx = dash.callback_context
    print(ctx.triggered[0]['prop_id'])

    if 'intervals' not in ctx.triggered[0]['prop_id']:
        trigger = ctx.triggered[0]['prop_id'].split('.')[0]
        i = trigger.split('-')[1]
        j = trigger.split('-')[2]
        print(i, j)
        dummy_engine.update_board(int(i), int(j))

    else:
        button_id = 'No clicks'
        print(button_id)

    game_board = dummy_engine.get_game()
    board = pd.DataFrame(game_board.get_board())
    p1_name = game_board.get_p1_name()
    p2_name = game_board.get_p2_name()
    p1_label = game_board.get_p1_label()
    p2_label = game_board.get_p2_label()
    turn = game_board.get_turn()
    first_turn = game_board.get_first_turn()
    state = game_board.get_state()
    return html.Div(id='game-body', children=[
        html.Div(id='game-state', children=[
            html.H4(states[state])
        ]),
        html.Div(id='game-turn', children=[
            html.H4('First Turn' + ": " + turns[first_turn]),
            html.H4('Turn' + ": " + turns[turn])
        ]),
        html.Div(id='game-players', children=[
            html.H4(p1_name + ": " + defs[p1_label]),
            html.H4(p2_name + ": " + defs[p2_label])
        ]),
        html.Div(id='game-board', children=[
            html.Table(GameServer.to_table(board))
        ])
    ])