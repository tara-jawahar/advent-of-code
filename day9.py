import numpy as np

def find_invalid_num(input, n):
    input = map(lambda x: int(x), input)
    previous_nums = []
    for i in range(n, len(input)):
        previous_nums = input[i-n:i]
        # print(previous_nums)
        if int(input[i]) < min(previous_nums):
            return input[i]
        possible_nums = map(lambda x : input[i] - x, filter(lambda x : x <= input[i], previous_nums))
        # print(possible_nums)

        valid_num = False
        for pn in possible_nums:
            if pn in previous_nums:
                valid_num = True
        if valid_num == False:
            return input[i]
    
    # No invalid numbers
    return None

def find_contiguous_sum(input, n):
    sum = find_invalid_num(input, n)
    print(sum)
    input = map(lambda x: int(x), input)
    if sum == None: return None

    sublists = []
    temp = []
    for i in range(len(input)):
        if input[i] >= sum:
            if temp != []:
                sublists += [temp]
                temp = []
        else:
            temp += [input[i]]
    # print(sublists)

    cont_nums = filter(lambda x : np.sum(x) >= sum, sublists)
    # print(cont_nums)

    for L in cont_nums:
        for i in range(0, len(L)):
            temp_list, temp_sum, start = [L[i]], L[i], 0
            for j in range(i+1, len(L)):
                if temp_sum < sum:
                    temp_list += [input[j]]
                    temp_sum += input[j]
                else:
                    break
            if temp_sum == sum:
                # print(temp_list)
                return min(temp_list) + max(temp_list)
    return None
        

if __name__ == '__main__':
    with open('inputs/day9_sample.txt') as f:
        sample = [line.strip() for line in f.readlines()]
    with open('inputs/day9_input.txt') as f:
        input = [line.strip() for line in f.readlines()]
    # print(find_invalid_num(sample, 5))
    # print(find_invalid_num(input, 25))
    # print(find_contiguous_sum(sample, 5))
    print(find_contiguous_sum(input, 25))