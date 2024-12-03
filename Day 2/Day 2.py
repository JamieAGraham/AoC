# Part 1 - Reasonably efficient

def is_safe_string(s: str) -> bool:
    numbers = list(map(int, s.split())) # ints plz
    
    if len(numbers) < 2:
        return True  # A single number or empty string is trivially "safe"
    
    trend = None  # Initial state
    
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        
        # Check the absolute difference constraint
        if abs(diff) < 1 or abs(diff) > 3:
            return False  # Unsafe due to difference rule
        
        # Determine the current trend
        if diff > 0:  # Increasing
            current_trend = True
        elif diff < 0:  # Decreasing
            current_trend = False
        
        if trend is None:
            trend = current_trend  # Set the initial trend
        elif trend != current_trend:
            return False  # Unsafe due to mixed trends
    
    return True 

# Part 2

def is_safe_string_with_removal(s: str) -> bool:
    # Let's brute force this *****
    if is_safe_string(s):
        return True
    
    numbers = list(map(int, s.split()))
    
    # Try removing each number and check if the string becomes safe
    for i in range(len(numbers)):
        modified_numbers = numbers[:i] + numbers[i+1:]
        modified_string = " ".join(map(str, modified_numbers))
        
        if is_safe_string(modified_string):
            return True  # Found a modification that makes it safe
    
    return False  # No single removal makes it safe


# This code will stay here as a monument to my failure. I was sure a more efficient method existed but it's simply 
# worse than the O(N^2) solution above

# def is_safe_string_with_one_removal(s: str) -> bool:
#     def is_safe(numbers):
#         """Check if a sequence of numbers is safe."""
#         trend = None  # To track increasing/decreasing
#         for i in range(1, len(numbers)):
#             diff = numbers[i] - numbers[i - 1]
#             if abs(diff) < 1 or abs(diff) > 3:  # Difference constraint
#                 return False
#             current_trend = diff > 0  # True for increasing, False for decreasing
#             if trend is None:
#                 trend = current_trend  # Set initial trend
#             elif trend != current_trend:
#                 return False  # Mixed trends detected
#         return True

#     def can_be_safe(numbers):
#         """Check if the sequence is safe or can be made safe by one removal."""
#         for i in range(1, len(numbers)):
#             diff = numbers[i] - numbers[i - 1]
#             # Check for violations
#             if abs(diff) < 1 or abs(diff) > 3 or (i > 1 and (diff > 0) != (numbers[i - 1] - numbers[i - 2] > 0)):
#                 # Simulate removing the previous element
#                 remove_prev = numbers[:i - 1] + numbers[i:]
#                 # Simulate removing the current element
#                 remove_curr = numbers[:i] + numbers[i + 1:]
#                 # Check if either sequence is safe
#                 return is_safe(remove_prev) or is_safe(remove_curr)
#         return True  # No violations found

#     # Convert the string into a list of integers
#     numbers = list(map(int, s.split()))
#     return can_be_safe(numbers)


tot = 0
tot_with_removal = 0
tot_with_removal_efficient = 0
with open("Day 2\\input.txt", "r") as f:
    all = list(f)
    for line in all:
        ans = is_safe_string(line)
        tot += ans
        tot_with_removal += is_safe_string_with_removal(line)

print(tot)
print(tot_with_removal)
print(tot_with_removal_efficient)
