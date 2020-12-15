from itertools import permutations
import copy

def decode(input):
    memory = {}
    for line in input:
        if line[:4] == 'mask':
            mask = line.split(' = ')[1]
        else:
            raw_val = list(bin(int(line.split(' = ')[1])).replace('0b', ''))
            val = ['0']*(len(mask) - len(raw_val))
            val += raw_val
            assert len(val) == 36
            loc = int(line.split(']')[0].split('[')[1])
            assert len(mask) == len(val)
            for i,char in enumerate(mask):
                if char == 'X': continue
                elif char == '1' or char == '0':
                    val[i] = char
            memory[loc] = ''.join(val)
    return sum(list(map(lambda x: int(x, 2), memory.values())))

def get_combo(loc, i):
    add1 = loc[:i] + '1' + loc[i+1:]
    add2 = loc[:i] + '0' + loc[i+1:]
    return [add1, add2]

# Given an address with X's, need all possible addresses
def get_addresses(x_indices, loc):
    addrs = []
    while len(x_indices) != 0:
        x = x_indices.pop(0)
        if addrs != []:
            temp = []
            for addr in addrs:
                temp += get_combo(addr,x)
            addrs = temp
        else:
            addrs = get_combo(loc, x)
    # print(addrs)
    return addrs

"""
XX -> 0X, 1X -> 00, 01, 10, 11
0X1 -> 001, 011
"""

def decode2(input):
    memory, addrs = {}, []
    for line in input:
        if line[:4] == 'mask':
            mask = line.split(' = ')[1]
        else:
            raw_loc = list(bin(int(line.split('[')[1].split(']')[0])).replace('0b', ''))
            loc = ['0']*(len(mask) - len(raw_loc))
            loc += raw_loc
            # assert len(loc) == 36
            val = int(line.split(' = ')[1])
            x_indices = []
            for i,char in enumerate(mask):
                if char != '0': loc[i] = char
                if char == 'X': x_indices += [i]
            addrs = get_addresses(x_indices, ''.join(loc))
        for addr in addrs:
            addr = int(''.join(addr),2)
            memory[addr] = val
    return sum(list(memory.values()))

if __name__ == '__main__':
    with open('inputs/day14_sample.txt') as f:
        sample = [line.strip() for line in f.readlines()]
    with open('inputs/day14_input.txt') as f:
        input = [line.strip() for line in f.readlines()]
    # print(decode(input))
    # print(decode2(sample))
    # get_addresses([0,1], 'XX')
    print(decode2(input))