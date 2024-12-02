# Location IDs
def compare_lists(left, right):
    left_sorted = sorted(left)
    right_sorted = sorted(right)

    dist = sum(abs(l-r) for l, r in zip(left_sorted, right_sorted))
    return dist

from collections import Counter

def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    # Python counters kind of cheat this task, I think
    right_count = Counter(right_list)

    # Calculate the similarity score
    similarity_score = sum(num * right_count[num] for num in left_list)
    return similarity_score

with open("Day 1\\input.txt", "r") as f:
    # Horrible ugly input parsing, don't judge me
    input = list(f)
    input = [a.split(" ") for a in input] 
    input = [[int(a[0]), int(a[3].removesuffix("\n"))] for a in input]

left, right = list(map(list, zip(*input)))
print(compare_lists(left, right))
print(calculate_similarity_score(left, right))