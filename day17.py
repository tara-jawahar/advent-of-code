import numpy as np, copy

def in_bounds(n_plane, n_row, n_col, plane, row, col):
    if row >= 0 and col >= 0 and plane >= 0 and row < n_row and col < n_col and plane < n_plane:
        return True
    return False

def find_neighbors(input, n_plane, n_row, n_col, plane, row, col, w_val):
    # Populate list of possible neighbors
    neighbors = 0
    for z in [-1,0,1]:
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                for w in [-1,0,1]:
                    if x==0 and y==0 and z==0 and w == 0: continue
                    if in_bounds(n_plane, n_row, n_col,plane+z,row+x,col+y) and input[plane+z][row+x][col+y] == '#':
                        neighbors += 1
    # neighbors += len(w_val)
    return neighbors

def next_round(input, curr_w):
    n_plane, n_row, n_col, active_ct = len(input), len(input[0]), len(input[0][0]), 0
    new_board = []
    for plane in range(n_plane):
        temp_plane = []
        for row in range(n_row):
            temp_row = ''
            for col in range(n_col):
                curr_space = input[plane][row][col]
                neighbors = find_neighbors(input, n_plane, n_row, n_col, plane, row, col, curr_w)
                if curr_space == '#':
                    if neighbors == 2 or neighbors == 3:
                        temp_row += '#'
                        active_ct += 1
                    else:
                        temp_row += '.'
                else:
                    if neighbors == 3:
                        temp_row += '#'
                        active_ct += 1
                    else:
                        temp_row += '.'
            # print(temp_row, active_ct)
            temp_plane += [temp_row]
        # print(temp_plane)
        new_board += [temp_plane]
    # print('final active count', active_ct)
    return active_ct, new_board

def simulate_cubes(input, rounds):
    n_row, n_col = len(input)+2, len(input[0])+2
    curr_board = [['.'*n_col]*n_row, ['.'*n_col]*n_row, ['.'*n_col] + list(map(lambda x: '.' + x + '.', input)) + ['.'*n_col], ['.'*n_col]*n_row, ['.'*n_col]*n_row]
    # curr_w = [0]
    # print(curr_board)
    active_ct_total = 0
    for i in range(rounds):
        active_ct, new_board = next_round(curr_board)
        # print(new_board)
        active_ct_total = active_ct
        curr_board = new_board

        # Add new empty planes if there are active states in outermost planes of current board
        
        # Add z coords
        curr_board.insert(0,['.'*n_col]*n_row)
        curr_board.append(['.'*n_col]*n_row)
        n_row += 2
        n_col += 2
        # Add x coords
        curr_board = [list(map(lambda x: '.' + x + '.', curr_board[i])) for i in range(len(curr_board))]
        # Add y coords
        curr_board = list(map(lambda L: ['.'*n_col] + L + ['.'*n_col], curr_board))

    print(len(curr_board), active_ct_total)
    return active_ct_total



if __name__ == '__main__':
    with open('inputs/day17_sample.txt') as f:
        sample = [line.strip() for line in f.readlines()]
    with open('inputs/day17_input.txt') as f:
        input = [line.strip() for line in f.readlines()]
    simulate_cubes(input,6)