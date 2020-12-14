import numpy as np

def find_bus(input):
    min_bus = int(input[0])
    in_service = filter(lambda x: x != 'x', input[1].split(','))
    first = [0,0]
    for bus in in_service:
        check = (min_bus/int(bus) + 1)*int(bus)
        if check < first[1] or first[1] == 0:
            first = [int(bus), check]
    return (first[1]-min_bus)*first[0]

def next_combo(curr_t, curr_i, bus, offset):
    # Calculates next time 2 buses will align given their IDs and 
    # time from current timestamp (curr_i, delay2)
    start = curr_i
    while True:
        # Iteratively add multiples of current timestamp
        start += curr_t
        # Find bus ID when two buses align
        if start % bus == offset:
            return start

"""
Solution with help from reddit thread (chrisfpdx)
My solution attempted to use Chinese Remainder Theorem/products but I did not
fully understand how the CRT was being implemented in Python.
"""
def find_bus_seq(input):
    in_service = input[1].split(',')
    # bus_nums_only = map(lambda x: int(x), filter(lambda x: x!= 'x', in_service))
    # prod = np.prod(bus_nums_only)
    # print(prod)
    curr_i = 0
    curr_t = int(in_service[0])
    for i,bus in enumerate(in_service[1:], start=1):
        print("i, bus:", i, bus)
        if bus != 'x':
            print(int(bus), i, int(bus)-i )
            # calculate difference between bus and time from timestamp (i)
            diff = int(bus) - i
            while diff < 0:
                # find out how much greater than i the bus id will be
                diff += int(bus)

            # print(curr_t, curr_i, int(bus), diff)
            next = next_combo(curr_t, curr_i, int(bus), diff)
            # New timestamp
            curr_t = curr_t * int(bus)
            curr_i = next - curr_t
    return next

if __name__ == '__main__':
    with open('inputs/day13_sample.txt') as f:
        sample = [line.strip() for line in f.readlines()]
    with open('inputs/day13_input.txt') as f:
        input = [line.strip() for line in f.readlines()]
    find_bus_seq(['968', '17,13'])
    # find_bus_seq(['968', '17,13,15'])
    # print(find_bus_seq(sample))
    # assert find_bus_seq(['968', '17,x,13,19']) == 3417
    # assert find_bus_seq(['968', '67,7,59,61']) == 754018
    # assert find_bus_seq(['968', '67,x,7,59,61']) == 779210
    # assert find_bus_seq(['968', '67,7,x,59,61']) == 1261476
    # assert find_bus_seq(['968', '1789,37,47,1889']) == 1202161486
    # print(find_bus_seq(input))
