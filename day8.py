import re, copy

def run_code(input):
    acc, idx = 0, 0
    visited = []
    while(idx < len(input)):
        instruction = input[idx].split(' ')[0]
        num = input[idx].split(' ')[-1]
        
        # Check if visited
        if idx in visited:
            return True, acc
        if instruction == 'acc':
            if num[0] == '-':
                acc -= int(num[1:])
            else:
                acc += int(num[1:])
        elif instruction == 'jmp':
            visited += [idx]
            if num[0] == '-':
                idx -= int(num[1:])
            else:
                idx += int(num[1:])
            continue
        # Add to visited list
        visited += [idx]
        idx += 1

    # No infinite loop
    return False, acc

def make_change(input):
    # Try changing 1 nop or jmp value in each run
    temp = copy.deepcopy(input)
    for i in range(len(input)):
        instruction = input[i].split(' ')[0]
        num = input[i].split(' ')[-1]
        if instruction == 'nop':
            temp[i] = 'jmp %s' % num
            if run_code(temp)[0] == False:
                print("NOP->JMP", i)
                return run_code(temp)[1]
            temp = copy.deepcopy(input)

    for i in range(len(input)):
        instruction = input[i].split(' ')[0]
        num = input[i].split(' ')[-1]
        if instruction == 'jmp':
            temp[i] = 'nop %s' % num
            if run_code(temp)[0] == False:
                print("JMP->NOP", i)  
                return run_code(temp)[1]
            temp = copy.deepcopy(input)
        

if __name__ == '__main__':
    with open('inputs/day8_sample.txt') as f:
        sample = [line.strip() for line in f.readlines()]
    with open('inputs/day8_input.txt') as f:
        input = [line.strip() for line in f.readlines()]
    print(make_change(input))