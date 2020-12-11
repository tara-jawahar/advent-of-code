
def jolt_diff(input):
    sorted = list(map(lambda x : int(x), input))
    sorted += [0]
    sorted.sort()
    # print(sorted)
    one_ct, two_ct, three_ct = 0,0, 0
    for i in range(len(sorted)-1):
        # print(sorted[i], sorted[i+1])
        if sorted[i] + 1 == sorted[i+1]:
            one_ct += 1
        elif sorted[i] + 2 == sorted[i+1]:
            two_ct += 1
        elif sorted[i] + 3 == sorted[i+1]:
            three_ct += 1
    three_ct += 1
    print(one_ct, two_ct, three_ct)
    return one_ct * three_ct

def jolt_arrange(input):
    sorted = list(map(lambda x : int(x), input))
    sorted += [0, max(sorted)+3]
    sorted.sort()

    path_ct = 1
    # Possible ways to arrange numbers when >1 combo exists
    vals_to_combos = {1:1, 2:1, 3:2, 4:4, 5:7}
    start = 0
    for i in range(len(sorted)-1):
        # print(i+1, sorted[i], start)
        # for sequences with >1 possible permutation
        if sorted[i] + 1 != sorted[i+1]:
            path_ct *= vals_to_combos[(i+1)-start]
            start = i+1
    
    return path_ct

class Node(object):

    def __init__(self, value, one=None, two=None, three=None):
        self.val = value    # The node value
        self.one = one      # the +1 node
        self.two = two      # the +2 node
        self.three = three  # the +3 node

    def insert(self, n):
        if self.val != None:
            # Recurse down the tree
            if self.one != None:
                self.one.insert(n)
            if self.two != None:
                self.two.insert(n)
            if self.three != None:
                self.three.insert(n)
            
            # Insert value on appropriate branch
            if self.val + 1 == n:
                if self.one == None:
                    self.one = Node(n)
                # else:
                #     self.one.insert(n)
            if self.val + 2 == n:
                if self.two == None:
                    self.two = Node(n)
                # else:
                #     self.two.insert(n)
            if self.val + 3 == n:
                if self.three == None:
                    self.three = Node(n)
                # else:
                #     self.three.insert(n)
        else:
            self.val = n
        
    def printTree(self):
        if self.one:
            print("one", self.one.val)
            self.one.printTree()
        if self.two:
            print("two", self.two.val)
            self.two.printTree()
        if self.three:
            print("three", self.three.val)
            self.three.printTree()
    
def build_tree(root, L, val):
    # Build the tree by inserting values in the list
    if val+1 in L:
        root.insert(val+1)
    if val+2 in L:
        root.insert(val+2)
    if val+3 in L:
        root.insert(val+3)
    return root

def countLeaves(root):
    # Recursively count leaves on the tree to get number of paths
    # Base case: leaf
    if root.one == None and root.two == None and root.three == None:
        return 1    
    if root.one == None and root.two == None:
        return countLeaves(root.three)
    if root.one == None and root.three == None:
        return countLeaves(root.two)
    if root.two == None and root.three == None:
        return countLeaves(root.one)
    if root.one == None:
        return countLeaves(root.two) + countLeaves(root.three)
    if root.two == None:
        return countLeaves(root.one) + countLeaves(root.three)
    if root.three == None:
        return countLeaves(root.one) + countLeaves(root.two)
    return countLeaves(root.one) + countLeaves(root.two) + countLeaves(root.three)

def jolt_arrange_tree(input):
    # Iterate through numbers in list to build the tree
    sorted = list(map(lambda x : int(x), input))
    sorted += [0, max(sorted)+3]
    sorted.sort()
    print("sorted")
    root = Node(sorted[0])
    curr_node = root
    for i in range(len(sorted)):
        curr_node = root
        curr_node = build_tree(curr_node, sorted, sorted[i])
        print("index", i)
    # root.printTree()
    count = countLeaves(root)
    return count

if __name__ == '__main__':
    with open('inputs/day10_sample.txt') as f:
        sample = [line.strip() for line in f.readlines()]
    with open('inputs/day10_input.txt') as f:
        input = [line.strip() for line in f.readlines()]
    print(jolt_arrange(input))
    # print(jolt_arrange_tree(input))
