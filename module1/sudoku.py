# we will first record rows and colums as STRINGS
rows = 'ABCDEFGHI'
cols = '123456789'

# we will now define a helper function which when given 2 strings 'a' and 'b'
# will return a list of all possible concatenations of a letter 's' in 'a' with
# letter 't' in 'b'
def cross(a , b):
    return [s + t for s in a for t in b]

# creationg labels for boxes , row_units , col_units , square_units and peers
boxes = cross(rows , cols)
row_units = [cross(r , cols) for r in rows]
col_units = [cross(rows , c) for c in cols]
square_units = [cross(rs , cs) for rs in ('ABC' , 'DEF' ,'GHI' ) for cs in ('123' , '456' , '789')]
unitlist = row_units + col_units + square_units
print (*unitlist)
units = dict((s , [u for u in unitlist if s in u])for s in boxes)
peers = dict((s, set(sum(units[s] , [])) - set([s])) for s in boxes)

# converting the input string into a dictionary
def grid_values(grid):
    assert len(grind) == 81 , "Input string must be of 81 no/string long(9 x 9)"
    return dict(zip(boxes , grid))