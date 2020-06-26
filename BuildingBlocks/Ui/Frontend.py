import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
from dash import callback_context

import Engine

external_stylesheets = [__name__, 'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(external_stylesheets=external_stylesheets, prevent_initial_callbacks=True)


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

defs = {-10: ' ', 1: 'X', 0: 'O'}
states = {0: ' ', 1: p1_name + ' WIN!', 2: p2_name + ' WIN!', 3: 'DRAW!'}
turns = {0: p1_name, 1: p2_name}


def to_table(dataframe):
    rows = []
    for i in range(len(dataframe)):
        row = []
        for col in dataframe.columns:
            value = dataframe.iloc[i][col]
            cell = html.Td(html.Button(defs[value], id='cell-'+str(i)+'-'+str(col)), style={'border': '1px solid #bbb'})
            row.append(cell)
        rows.append(html.Tr(row))
    return html.Table(rows, id='board',)


app.layout = html.Div(id='all-game', children=[
    html.Header(id='game-header', children=[
        html.H1('TIC TAC TOE!')
    ]),
    html.Div(id='game-body', children=[
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
            html.Table(to_table(pd.DataFrame(board)))
        ])
    ]),
    dcc.Interval(
            id='interval-component',
            interval=1*4000,
            n_intervals=0
        )
])


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
                    html.Table(to_table(board))
                ])
            ])
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
                    html.Table(to_table(board))
                ])
            ])

if __name__ == '__main__':
    print("in main")
    app.run_server(debug=True)
