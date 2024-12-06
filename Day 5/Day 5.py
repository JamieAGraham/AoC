from typing import List, Tuple

# Read and parse input file
with open("Day 5\\input.txt", 'r') as file:
    input_lines: List[str] = list(file)

rules: List[str] = []
tests: List[str] = []
parsing_rules: bool = True

for line in input_lines:
    if parsing_rules and line != "\n":
        rules.append(line.strip())
    elif line == "\n":
        parsing_rules = False
    else:
        tests.append(line.strip())


# Ints not strs
parsed_rules: List[List[int]] = [list(map(int, rule.split("|"))) for rule in rules]


parsed_tests: List[List[int]] = [list(map(int, test.split(","))) for test in tests]


def check_input(test: List[List[int]], rules: List[List[int]]) -> int:
    """Checks the input against rules and calculates a result."""
    counter: int = 0
    for to_test in test:
        is_valid: bool = True
        for rule in rules:
            if rule[0] in to_test and rule[1] in to_test:
                if to_test.index(rule[0]) > to_test.index(rule[1]):
                    is_valid = False
        if is_valid:
            counter += to_test[(len(to_test) + 1) // 2 - 1]
    return counter

def return_false_input(test: List[List[int]], rules: List[List[int]]) -> List[List[int]]:
    """Returns the test cases that do not pass the rules."""
    failing_tests: List[List[int]] = []
    for to_test in test:
        is_valid: bool = True
        for rule in rules:
            if rule[0] in to_test and rule[1] in to_test:
                if to_test.index(rule[0]) > to_test.index(rule[1]):
                    is_valid = False
        if not is_valid:
            failing_tests.append(to_test)
    return failing_tests

def single_validation(inp: List[int], rules: List[List[int]]) -> bool:
    """Validates a single test case against rules."""
    for rule in rules:
        if rule[0] in inp and rule[1] in inp:
            if inp.index(rule[0]) > inp.index(rule[1]):
                return False
    return True

def swap_indices(array: List[int], val1: int, val2: int) -> List[int]:
    """Swaps two indices in a list and returns the updated list."""
    idx1, idx2 = array.index(val1), array.index(val2)
    array[idx1], array[idx2] = array[idx2], array[idx1]
    return array

def single_list_traverse(inp: List[int], rules: List[List[int]]) -> List[int]:
    """Traverses and adjusts a single test case to meet rules."""
    for rule in rules:
        if rule[0] in inp and rule[1] in inp:
            if inp.index(rule[0]) > inp.index(rule[1]):
                swap_indices(inp, rule[0], rule[1])
    return inp


print(check_input(parsed_tests, parsed_rules))

# Process failing inputs
failing_inputs: List[List[int]] = return_false_input(parsed_tests, parsed_rules)

# Cross fingers and pray the input is nice and we don't have any weird cyclic stuff, just swapping elements
corrected_tests: List[List[int]] = []
for test_case in failing_inputs:
    temp: List[int] = test_case
    while not single_validation(temp, parsed_rules):
        temp = single_list_traverse(temp, parsed_rules)
    corrected_tests.append(temp)

final_sum: int = sum([test[(len(test) + 1) // 2 - 1] for test in corrected_tests])
print(final_sum)
