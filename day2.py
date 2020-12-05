import csv

def challenge1(input):
    valid_ct = 0
    for i in range(len(input)):
        print(input[i])
        # Parse string
        parts = input[i][0].split(' ')
        policy_min = int(parts[0].split('-')[0])
        policy_max = int(parts[0].split('-')[1])
        policy_letter = parts[1][0]
        pw = parts[2]
        # print(policy_min, policy_max, policy_letter, pw)

        pw_list = list(pw)
        # print(pw, pw_list)
        letter_count = len(filter(lambda x: x == policy_letter, pw_list))
        # print(policy_letter, pw, policy_min, policy_max+1, letter_count, letter_count in range(policy_min, policy_max+1))
        if letter_count in range(policy_min, policy_max+1):
            valid_ct+=1

    return valid_ct

def challenge2(input):
    valid_ct = 0
    for i in range(len(input)):
        # print(input[i])
        # Parse string
        parts = input[i][0].split(' ')
        policy1 = int(parts[0].split('-')[0])-1
        policy2 = int(parts[0].split('-')[1])-1
        policy_letter = parts[1][0]
        pw = parts[2]

        pw_list = list(pw)
        # print(pw, pw_list)
        print(policy_letter, pw, policy1, policy2)
        if (pw_list[policy1] == policy_letter) ^ (pw_list[policy2] == policy_letter):
            valid_ct +=1

    return valid_ct
        

if __name__ == '__main__':
    sample = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    with open('inputs/day2_input.csv') as f:
        reader = csv.reader(f)
        input = list(reader)
    # print(challenge1(input))
    print(challenge2(input))