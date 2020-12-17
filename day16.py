from collections import defaultdict

def invalid_tix(input):
    # Determine valid ranges
    valid = []
    specs = defaultdict()
    for line in input:
        if len(line) == 0: break
        ranges = line.split(': ')[1].split(' or ')
        range1 = range(int(ranges[0].split('-')[0]), int(ranges[0].split('-')[-1])+1)
        range2 = range(int(ranges[1].split('-')[0]), int(ranges[1].split('-')[-1])+1)
        specs[line.split(': ')[0]] = set(list(range1) + list(range2))
        valid += list(range1) + list(range2)
    valid_set = set(valid)

    # Check nearby tickets
    nearby_start = False
    valid_tickets = []
    my_ticket_idx = 0
    for i,line in enumerate(input):
        if 'your ticket' in line:
            my_ticket_idx = i+1
            continue
        if 'nearby tickets' in line: 
            nearby_start = True
            continue
        if nearby_start:
            # if all numbers are not valid, don't add to valid tickets
            if len(list(filter(lambda x: int(x) not in valid_set, line.split(',')))) == 0:
                valid_tickets += [line]
    my_ticket = list(input[my_ticket_idx].split(','))
    return valid_tickets, my_ticket, specs

def match_positions(input):
    valid_tickets, my_ticket, specs = invalid_tix(input)
    matches = defaultdict()
    cols = []
    for i in range(len(valid_tickets[0].split(','))):
        temp = []
        for t in valid_tickets:
            temp += [int(t.split(',')[i])]
        cols += [temp]

    assert len(cols) == len(valid_tickets[0].split(','))
    assert len(cols[0]) == len(valid_tickets)
    
    for i,col in enumerate(cols):
        for p,s in specs.items():
            # add all possible values
            if len(list(filter(lambda val: val not in s, col))) == 0: 
                if matches.get(p) == None: matches[p] = [i]
                else: matches[p] += [i]

    # sort matches by possible positions and use process of elimination
    sorted_matches = dict(sorted(matches.items(), key=lambda item: len(item[1])))
    taken = set()
    final_matches = defaultdict()
    for k,v in sorted_matches.items():
        val = list(set(v).difference(taken))[0]
        taken.add(val)
        final_matches[k] = int(val)
    
    # calculate desired product of certain fields in 'your ticket'
    prod = 1
    for k,v in final_matches.items():
        if 'departure' in k:
            prod *= int(my_ticket[v])
    return prod

if __name__ == '__main__':
    with open('inputs/day16_sample.txt') as f:
        sample = [line.strip() for line in f.readlines()]
    with open('inputs/day16_input.txt') as f:
        input = [line.strip() for line in f.readlines()]
    # print(invalid_tix(sample))
    # print(match_positions(sample))
    print(match_positions(input))