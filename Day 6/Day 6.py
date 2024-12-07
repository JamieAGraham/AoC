from collections import Counter
with open('Day 6\\input.txt', 'r') as f:
    inp = list(f)
inp = [list(a.removesuffix("\n")) for a in inp]


dirs = {'^':{'dir':(-1,0), 'rot':'>'},
        'v':{'dir':(1,0), 'rot':'<'},
        '<':{'dir':(0,-1), 'rot':'^'},
        '>':{'dir':(0,1), 'rot':'v'}}

def find_arrow(array):
    c = Counter([x for xs in array for x in xs])
    #assert((c['^'] + c['>'] + c['v'] + c['<']) == 1, "Input not valid")
    char = [k for k, v in c.items() if v==1][0]
    return [(row_index, col_index) for row_index, row in enumerate(array) for col_index, col in enumerate(row) if char in row and col==char][0]



# row, col = find_arrow(inp)
# print(inp[row][col])

def step(array):
    row, col = find_arrow(array)
    char = array[row][col]
    dir = dirs[char]['dir']
    new_row = row+dir[0]
    new_col = col+dir[1]
    print(row, col, char, new_row, new_col)
    row_size = len(array)
    col_size = len(array[0])
    # Assuming here that there are no cyclic paths?
    if (new_row == -1) or (new_col == -1) or (new_row == row_size) or (new_col == row_size):
        return (True, array)
    if array[new_row][new_col] == '#':
        array[row][col] = dirs[char]['rot']
        return (False, array)
    if (array[new_row][new_col] == '.') or (array[new_row][new_col] == 'X'):
        array[new_row][new_col] = char
        array[row][col] = 'X'
        return (False, array)
    else:
        raise ValueError(f'Hmm...{char}')

flag = False
while flag == False:
    flag, inp = step(inp)
    

print(Counter([x for xs in inp for x in xs]))
with open('Day 6\\output.txt', 'w') as f:
    f.write('\n'.join([''.join(row) for row in inp]))