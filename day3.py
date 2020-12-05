import csv


def challenge1(input, right_num, down_num):
    # infinite number of columns, finite number of rows
    tree_ct = 0
    row, col = 0, 0
    base_cols = len(input[0][0])
    while row != len(input)-1:
        if input[row+down_num][0][(col+right_num)%base_cols] == '#':
            tree_ct+=1
        row+=down_num
        col+=right_num
    return tree_ct

if __name__ == '__main__':
    with open('inputs/day3_sample.csv') as f:
        reader = csv.reader(f)
        sample = list(reader)
    with open('inputs/day3_input.csv') as f:
        reader = csv.reader(f)
        input = list(reader)
    print(challenge1(input, 3, 1))
    print(challenge1(input,1,1)*challenge1(input,3,1)*challenge1(input,5,1)*challenge1(input,7,1)*challenge1(input,1,2))