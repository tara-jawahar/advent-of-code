import csv
import re

def bag_hierarchy(input, your_bag):
    # Build bag hierarchy after parsing strings
    bag_hier = {}
    for line in input:
        # String parsing
        line=line[0]
        outer = line.split(' bags contain ')[0]
        inner = line.split(' bags contain ')[1].split(', ')
        inner_dict = {}
        for i in inner:
            num = i.split(' ')[0]
            # for bags containing 0 bags
            if num == 'no':
                continue
            inner_dict[' '.join(i.split(' ')[1:-1])] = int(num)
        bag_hier[outer] = inner_dict
    return bag_hier

def can_hold_bag_color(bag_hier, outer_bag, bag_color, visited):
    # Recursive function that checks if bag is in hierarchy
    count = 0
    # No bags inside this bag
    if bag_hier.get(outer_bag) == None:
        visited += outer_bag
        return 0
    # Desired bag found - return 1
    if bag_color in bag_hier[outer_bag]:
        visited += outer_bag
        return 1
    # Loop through bags withing outer bags to find desired bag
    for i in bag_hier[outer_bag].keys():
        if i in visited:
            continue
        count += can_hold_bag_color(bag_hier, i, bag_color, visited)
    if count >= 1: 
        return 1
    else:
        return 0

def challenge1(sample, your_bag):
    bag_hier = bag_hierarchy(sample, 'shiny gold')
    bag_count = 0
    for bag_color in bag_hier.keys():
        if bag_color != your_bag:
            bag_count += can_hold_bag_color(bag_hier, bag_color, your_bag, [])
    return bag_count

def challenge2(bag_hier, your_bag):
    # Recursively call this function to count inner bags
    bag_count = 0
    for color, count in bag_hier[your_bag].items():
        bag_count += count*(1+challenge2(bag_hier, color))
    return bag_count

if __name__ == '__main__':
    with open('inputs/day7_sample.csv') as f:
        reader = csv.reader(f,delimiter='-')
        sample = list(reader)
    with open('inputs/day7_input.csv') as f:
        reader = csv.reader(f,delimiter='-')
        input = list(reader)
    bag_hier = bag_hierarchy(input, 'shiny gold')
    print(challenge2(bag_hier, 'shiny gold'))