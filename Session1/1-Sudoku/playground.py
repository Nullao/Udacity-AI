from utils import *

def cross(a, b):
    return [s+t for s in a for t in b]

rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

unitlist = row_units + column_units + square_units 

"""
def string_premutation(a):
    length = len(a)
    str_list = []
    for i in range(length):
        str_list.append(a[i:length] + a[0:i])
    return str_list
"""
def merge_diag(a, b):
    length = len(a)
    str_list = []
    for i in range(length):
        str_list.append(a[i] + b[i])
    return str_list 

diag_units = [merge_diag(rows, cols), merge_diag(rows, cols[::-1])]

unitlist = unitlist + diag_units


# Must be called after all units (including diagonals) are added to the unitlist
units = extract_units(unitlist, boxes)
peers = extract_peers(units, boxes)


row = extract_units(row_units, boxes)
row_peers = extract_peers(row, boxes)

col = extract_units(column_units, boxes)
col_peers = extract_peers(col, boxes)

square = extract_units(square_units, boxes)
square_peers = extract_peers(square, boxes)

diag = extract_units(diag_units, boxes)
diag_peers = extract_peers(diag, boxes)

print(diag_peers['A2'] == null)
