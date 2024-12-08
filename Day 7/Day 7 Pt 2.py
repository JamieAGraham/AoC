import operator
from itertools import product

# Input test cases
test = ["180: 60 2 1", "190: 10 19", "3267: 81 40 27", "156: 15 6", "7290: 6 8 6 15", "192: 17 8 14"]

# Parse input into a target and a list of integers
manip = [[int(a.split(":")[0]), list(map(int, a.split(":")[1].split()))] for a in test]

with open("Day 7\\input.txt", 'r') as f:
    inp = list(f)

manip = [[int(a.split(":")[0]), list(map(int, a.split(":")[1].split()))] for a in inp]
# Concatenation operator function
def concat(x, y):
    return int(f"{x}{y}")

# Function to generate all combinations of operators for a given length
def gen_combs(n):
    return product([operator.add, operator.mul, concat], repeat=n)

# Evaluate expression left-to-right using given operators and integers
def evaluate_expression(ints, ops):
    result = ints[0]
    for i in range(len(ops)):
        result = ops[i](result, ints[i + 1])
    return result

running_total = 0
# Check each test case
for target, nums in manip:
    n = len(nums) - 1  # Number of operator positions
    found = False

    for ops in gen_combs(n):
        try:
            if evaluate_expression(nums, ops) == target:
                found = True
                # Convert operator functions back to symbols for display
                op_symbols = []
                for op in ops:
                    if op == operator.add:
                        op_symbols.append('+')
                    elif op == operator.mul:
                        op_symbols.append('*')
                    elif op == concat:
                        op_symbols.append('||')

                print(f"Match found for {target}: {' '.join(map(str, nums))} with {' '.join(op_symbols)}")
                running_total += target
                break
        except Exception as e:
            # Catch and ignore any errors (e.g., invalid operations)
            pass
    
    if not found:
        print(f"No match found for {target}")

print("Running total: ", running_total)