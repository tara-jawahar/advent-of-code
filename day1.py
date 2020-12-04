import pandas as pd 

def challenge1(input):
    for i in range(len(input)-1):
        for j in range(1, len(input)):
            if int(input.iloc[i,0]) + int(input.iloc[j,0]) == 2020:
                return int(input.iloc[i,0]) * int(input.iloc[j,0])

    return "No matches found"

def challenge2(input):
    # Store all sums if less than 2020
    intmed_sums = []
    intmed_products = []
    for i in range(len(input)-1):
        for j in range(1, len(input)):
            if i == j: continue
            val1 = int(input.iloc[i,0])
            val2 = int(input.iloc[j,0])
            intmed_sums += [(val1, val2, val1+val2)]
            intmed_products += [(val1, val2, val1*val2)]

    # Filter sums list if element is greater than 2020 or less than min value
    min_val = input.iloc[:,0].min()
    max_val = input.iloc[:,0].max()
    for s in range(len(intmed_sums)):
        if intmed_sums[s][2] > (2020-min_val) or intmed_sums[s][2] < (2020-max_val):
            intmed_sums[s] = -1
            intmed_products[s] = -1
    intmed_sums = filter(lambda x: x != -1, intmed_sums)
    intmed_products = filter(lambda x: x != -1, intmed_products)

    for k in range(len(input)):
        for idx in range(len(intmed_sums)):
            if int(input.iloc[k,0]) + intmed_sums[idx][2] == 2020 and k != intmed_sums[idx][0] and k != intmed_sums[idx][1]:
                return int(input.iloc[k,0]) * intmed_products[idx][2]
            idx+=1
        k+=1
    
    return "No matches found"


if __name__ == "__main__":
    input = pd.read_csv("day1_input.csv")
    # sample = pd.DataFrame([200, 75, 800, 1100, 1020])
    # print(challenge1(input))
    print(challenge2(input))