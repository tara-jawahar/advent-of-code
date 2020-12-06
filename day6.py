import csv

def group_letters(input):
    accum = []
    all_groups = []
    for line in input:
        if line != []:
            accum += [line[0]]
        else:
            all_groups += [accum]
            accum = []
    all_groups += [accum]
    return all_groups

def challenge1(input):
    all_groups = group_letters(input)
    unique_letters = map(lambda x : len(set(list(x))), all_groups)
    return sum(unique_letters)

def challenge2(input):
    all_groups = group_letters(input)
    count = 0
    for group in all_groups:
        unique = set('abcdefghijklmnopqrstuvwxyz')
        for passenger in group:
            unique = unique.intersection(passenger)
        count += len(unique)
    return count

if __name__ == '__main__':
    with open('inputs/day6_sample.csv') as f:
        reader = csv.reader(f)
        sample = list(reader)
    with open('inputs/day6_input.csv') as f:
        reader = csv.reader(f)
        input = list(reader)
    # print(sample)
    # print(challenge1(input))
    print(challenge2(input))