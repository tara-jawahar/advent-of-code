
def change_dir(curr_dir, to_dir, degrees):
    all_dirs = ['N', 'W', 'S', 'E', 'N', 'W', 'S', 'E']
    rotations = {90 : 1, 180 : 2, 270 : 3, 360 : 4}
    for dir in range(4):
        if all_dirs[dir] == curr_dir:
            if to_dir == 'L':
                return all_dirs[(dir+rotations[degrees%360])]
            else:
                return all_dirs[(dir-rotations[degrees%360])]

def change_waypt_dir(waypt_position, to_dir, degrees):
    # Ex. (2,-1) rotates left to (1,2) left to (-2,1), left to (-1,-2)
    x,y = waypt_position[0], waypt_position[1]
    rotations_cwise = {0: [x,y], 90 : [y,-x], 180 : [-x,-y], 270 : [-y,x]}
    rotations_ccwise = {0: [x,y], 90 : [-y,x], 180 : [-x,-y], 270 : [y,-x]}
    if to_dir == 'L':
        return rotations_ccwise[degrees%360]
    else:
        return rotations_cwise[degrees%360]
        
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


def move_ship_waypt(input):
    # curr_dir = 'E'
    # position follows Cartesian coordinates (W/E on x axis, N/S on y axis)
    ship_position = [0,0]
    waypt_position = [10,1]
    for dir in input:
        if dir[0] == 'L':
            waypt_position = change_waypt_dir(waypt_position, 'L', int(dir[1:]))
        elif dir[0] == 'R':
            waypt_position = change_waypt_dir(waypt_position, 'R', int(dir[1:]))
        elif dir[0] == 'F':
            ship_position[0] += int(dir[1:])*waypt_position[0]
            ship_position[1] += int(dir[1:])*waypt_position[1]
        else:
            waypt_position = move_forward(waypt_position, dir[0], int(dir[1:]))
    # print(ship_position)
    # print(waypt_position)
    return abs(ship_position[0]) + abs(ship_position[1])

if __name__ == '__main__':
    with open('inputs/day12_sample.txt') as f:
        sample = [line.strip() for line in f.readlines()]
    with open('inputs/day12_input.txt') as f:
        input = [line.strip() for line in f.readlines()]
    print(move_ship_waypt(input))