import operator
from itertools import product

# Input test cases
test = ["180: 60 2 1", "190: 10 19", "3267: 81 40 27"]

# Parse input into a target and a list of integers
manip = [[int(a.split(":")[0]), list(map(int, a.split(":")[1].split()))] for a in test]

with open("Day 7\\input.txt", 'r') as f:
    inp = list(f)

manip = [[int(a.split(":")[0]), list(map(int, a.split(":")[1].split()))] for a in inp]

def gen_combs(n):
    return product([operator.add, operator.mul], repeat=n)

# Messed this up initially and automatically went for BODMAS. Simplify!
def evaluate_expression(ints, ops):
    result = ints[0]
    for i in range(len(ops)):
        result = ops[i](result, ints[i + 1])
    return result

running_total = 0
for target, nums in manip:
    n = len(nums) - 1
    found = False

    for ops in gen_combs(n):
        if evaluate_expression(nums, ops) == target:
            found = True
            op_symbols = ['+' if op == operator.add else '*' for op in ops]
            print(f"Match found for {target}: {' '.join(map(str, nums))} with {' '.join(op_symbols)}")
            running_total += target
            break
    
    if not found:
        print(f"No match found for {target}")

print("Running Total: ", running_total)