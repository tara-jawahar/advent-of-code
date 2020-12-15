
def memory_game(input, limit):
    past_nums = {}
    visited = set()
    # populate with input
    for i,n in enumerate(input[:-1]):
        past_nums[n] = [i+1]
        visited.add(n)
        # print(i+1, n)
    # print(past_nums)
    curr_num = input[-1]
    for turn in range(len(input)+1, limit+1):
        # print("entering loop", turn, curr_num)
        # print("bottleneck?")
        if curr_num in visited:
            # print('visited before')
            # print(turn, past_nums[curr_num])
            if len(past_nums[curr_num]) < 2:
                curr_num = (turn-1) - past_nums[curr_num][-1]
            else:
                curr_num = past_nums[curr_num][-1] - past_nums[curr_num].pop(-2)
            if past_nums.get(curr_num) == None:
                past_nums[curr_num] = [turn]
                visited.add(curr_num)
            else:
                past_nums[curr_num] += [turn]
        else:
            # print('new num')
            past_nums[curr_num] = [turn-1]
            visited.add(curr_num)
            curr_num = 0
            past_nums[0] += [turn]
        # print(visited, set(past_nums.keys()))
        # print(turn, curr_num, past_nums)
    return curr_num

if __name__ == '__main__':
    sample = [0,3,6]
    input = [0,6,1,7,2,19,20]
    # print(memory_game(sample, 2020))
    print(memory_game(input, 30000000))