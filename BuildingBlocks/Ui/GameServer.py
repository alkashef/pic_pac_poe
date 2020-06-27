import dash
import Engine
import pandas as pd

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