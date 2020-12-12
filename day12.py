
def change_dir(curr_dir, to_dir, degrees):
    all_dirs = ['N', 'W', 'S', 'E', 'N', 'W', 'S', 'E']
    rotations = {90 : 1, 180 : 2, 270 : 3, 360 : 4}
    for dir in range(4):
        if all_dirs[dir] == curr_dir:
            if to_dir == 'L':
                return all_dirs[(dir+rotations[degrees%360])]
            else:
                return all_dirs[(dir-rotations[degrees%360])]

def move_forward(position, dir, distance):
    if dir == 'N':
        position[1] += distance
    elif dir == 'S':
        position[1] -= distance
    elif dir == 'E':
        position[0] += distance
    elif dir == 'W':
        position[0] -= distance
    return position


def move_ship(input):
    curr_dir = 'E'
    # position follows Cartesian coordinates (W/E on x axis, N/S on y axis)
    position = [0,0]
    for dir in input:
        if dir[0] == 'L':
            curr_dir = change_dir(curr_dir, 'L', int(dir[1:]))
        elif dir[0] == 'R':
            curr_dir = change_dir(curr_dir, 'R', int(dir[1:]))
        else:
            if dir[0] == 'F':
                position = move_forward(position, curr_dir, int(dir[1:]))
            else:
                position = move_forward(position, dir[0], int(dir[1:]))
    # print(position)
    return abs(position[0]) + abs(position[1])

if __name__ == '__main__':
    with open('inputs/day12_sample.txt') as f:
        sample = [line.strip() for line in f.readlines()]
    with open('inputs/day12_input.txt') as f:
        input = [line.strip() for line in f.readlines()]
    print(move_ship(input))