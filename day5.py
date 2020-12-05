import csv

def get_val(row, total, vals):
    for i in row:
        low = min(total)
        high = max(total)
        half = (high-low)/2
        if i == vals[0]:
            total = range(low, low+half+1)
        else:
            total = range(low+half+1, high+1)
        # print(i, total)
    return total[0]

def challenge1(input):
    max_seat_id = 0
    for line in input:
        line = line[0]
        row = line[:7]
        col = line[7:]

        total_rows = range(0,128)
        total_cols = range(0, 8)

        row_val = get_val(row, total_rows, ['F', 'B'])
        col_val = get_val(col, total_cols, ['L', 'R'])

        seat_id = row_val * 8 + col_val

        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id

def challenge2(input):
    # Using the fact that Python dictionary keys are ordered sets
    seat_ids = {}
    for line in input:
        line = line[0]
        row = line[:7]
        col = line[7:]

        total_rows = range(0,128)
        total_cols = range(0, 8)

        row_val = get_val(row, total_rows, ['F', 'B'])
        col_val = get_val(col, total_cols, ['L', 'R'])

        seat_id = row_val * 8 + col_val

        seat_ids[seat_id] = None
    all_seats = range(min(seat_ids.keys()), max(seat_ids.keys()))
    open_seats = set(all_seats) - set(list(seat_ids.keys()))
    my_seat = 0
    for seat in open_seats:
        if seat-1 not in open_seats and seat+1 not in open_seats:
            my_seat = seat
    return my_seat


if __name__ == '__main__':
    with open('inputs/day5_sample.csv') as f:
        reader = csv.reader(f)
        sample = list(reader)
    with open('inputs/day5_input.csv') as f:
        reader = csv.reader(f)
        input = list(reader)
    # print(challenge1([['FBFBBFFRLR']]))
    print(challenge2(input))