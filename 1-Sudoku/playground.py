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
print (diag_units)