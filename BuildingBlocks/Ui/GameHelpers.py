import dash_html_components as html
from GameServer import p1_name, p2_name


def get_turn(num):
    if num == 0:
        return p1_name
    else:
        return p2_name

def get_def(num):
    if num == -10:
        return ' '
    elif num ==  1:
        return 'X'
    else:
        return 'O'

def get_state(num):
    if num == 0:
        return ' '
    elif num ==  1:
        return  p1_name + ' WIN!'
    elif num == 2:
        return p2_name + ' WIN!'
    else:
        return 'DRAW!'

def to_table(dataframe):
    rows = []
    for i in range(len(dataframe)):
        row = []
        for col in dataframe.columns:
            value = dataframe.iloc[i][col]
            cell = html.Td(html.Button(get_def(value), id='cell-'+str(i)+'-'+str(col)), style={'border': '1px solid #bbb'})
            row.append(cell)
        rows.append(html.Tr(row))
    return html.Table(rows, id='board',)