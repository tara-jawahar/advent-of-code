import copy

def in_bounds(row_len, col_len, row, col):
    if row >= 0 and col >= 0 and row < row_len and col < col_len:
        return True
    return False

def next_round(input):
    new_board = [[None]*len(input[0])]*len(input)
    rows, cols = range(len(input)), range(len(input[0]))
    # rows, cols = [0], [2]
    final = []
    for row in rows:
        for col in cols:
            if input[row][col] == '.' : new_board[row][col] = '.'
            # find occupied adjacent seats by checking value in seat in every direction
            poss_adj = [(row-1,col-1),(row-1,col),(row-1,col+1),(row,col-1),(row,col+1),(row+1,col-1),(row+1,col),(row+1,col+1)]
            valid_adj = filter(lambda x: x[0] < len(input) and x[0] >= 0 and x[1] < len(input[0]) and x[1] >= 0, poss_adj)
            occupied_adj = filter(lambda x: x == '#', map(lambda (x,y) : input[x][y], valid_adj))
            if input[row][col] == 'L':
                # seat is empty, check adjacent seats
                if len(occupied_adj) == 0:
                    new_board[row][col] = '#'
                else:
                    new_board[row][col] = 'L'
            if input[row][col] == '#':
                # seat is full, check adjacent seats
                if len(occupied_adj) >= 4:
                    new_board[row][col] = 'L'
                else:
                    new_board[row][col] = '#'
        final += [''.join(new_board[row])]
    return final

def find_first_seats(input, row, col):
    # Given row, col find first seat in every direction
    pos = {'top_left': None, 'top': None, 'top_right': None, 'left': None, 'right': None,
        'bottom_left': None, 'bottom': None, 'bottom_right': None}
    row_len, col_len = len(input), len(input[0])
    for i in range(1,min(row_len, col_len)):
        if pos['top_left'] == None and in_bounds(row_len, col_len, row-i, col-i) and input[row-i][col-i] != '.':
            pos['top_left'] = input[row-i][col-i]
        if pos['top'] == None and in_bounds(row_len, col_len, row-i, col) and input[row-i][col] != '.':
            pos['top'] = input[row-i][col]
        if pos['top_right'] == None and in_bounds(row_len, col_len, row-i, col+i) and input[row-i][col+i] != '.':
            pos['top_right'] = input[row-i][col+i]
        if pos['left'] == None and in_bounds(row_len, col_len, row, col-i) and input[row][col-i] != '.':
            pos['left'] = input[row][col-i]
        if pos['right'] == None and in_bounds(row_len, col_len, row, col+i) and input[row][col+i] != '.':
            pos['right'] = input[row][col+i]
        if pos['bottom_left'] == None and in_bounds(row_len, col_len, row+i, col-i) and input[row+i][col-i] != '.':
            pos['bottom_left'] = input[row+i][col-i]
        if pos['bottom'] == None and in_bounds(row_len, col_len, row+i, col) and input[row+i][col] != '.':
            pos['bottom'] = input[row+i][col]
        if pos['bottom_right'] == None and in_bounds(row_len, col_len, row+i, col+i) and input[row+i][col+i] != '.':
            pos['bottom_right'] = input[row+i][col+i]
    return pos

def next_round2(input):
    new_board = [[None]*len(input[0])]*len(input)
    rows, cols = range(len(input)), range(len(input[0]))
    final = []
    for row in rows:
        for col in cols:
            if input[row][col] == '.' : new_board[row][col] = '.'
            pos = find_first_seats(input, row, col)
            if input[row][col] == 'L':
                # seat is empty, check first seats you can see
                if len(filter(lambda x: x == '#', list(pos.values()))) == 0:
                    new_board[row][col] = '#'
                else:
                    new_board[row][col] = 'L'
            if input[row][col] == '#':
                # seat is full, check first seats you can see 
                if len(filter(lambda x: x == '#', list(pos.values()))) >= 5:
                    new_board[row][col] = 'L'
                else:
                    new_board[row][col] = '#'
        final += [''.join(new_board[row])]
    return final

def find_stable(input):
    curr_board = input
    prev = []
    while curr_board != prev:
        prev = copy.deepcopy(curr_board)
        curr_board = next_round2(curr_board)
    
    # Count occupied seats
    seat_ct = 0
    for row in curr_board:
        for char in row:
            if char == '#':
                seat_ct += 1
    return seat_ct


if __name__ == '__main__':
    with open('inputs/day11_sample.txt') as f:
        sample = [line.strip() for line in f.readlines()]
    with open('inputs/day11_input.txt') as f:
        input = [line.strip() for line in f.readlines()]
    print(find_stable(input))