def parse_muls(input_string: str) -> int: 
    result = 0
    i = 0

    while i < len(input_string):
        if input_string[i:i+4] == "mul(":
            i+=4
            num1 = ""
            while i < len(input_string) and input_string[i].isdigit():
                num1 += input_string[i]
                i += 1
            
            if i < len(input_string) and input_string[i] == ',':
                i += 1  # Move past the comma
                num2 = ""

                while i < len(input_string) and input_string[i].isdigit():
                    num2 += input_string[i]
                    i += 1

                if i < len(input_string) and input_string[i] == ')':
                    i += 1  # Move past the closing parenthesis
                    if num1.isdigit() and num2.isdigit():
                        result += int(num1) * int(num2)
                    continue  # Skip to next potential match
        i += 1
    
    return result

def parse_mul_do(input_string: str) -> int:
    result = 0
    is_enabled = True
    i = 0

    while i < len(input_string):
        # Check for "don't()"
        if input_string[i:i+6] == "don't(":
            is_enabled = False
            i += 6  # Skip past "don't("
            continue
        
        # Check for "do()"
        elif input_string[i:i+3] == "do(":
            is_enabled = True
            i += 3  # Skip past "do("
            continue
        
        # Check for "mul("
        elif input_string[i:i+4] == "mul(":
            if is_enabled:  # Only process if enabled
                i += 4
                num1 = ""
                while i < len(input_string) and input_string[i].isdigit():
                    num1 += input_string[i]
                    i += 1
                
                if i < len(input_string) and input_string[i] == ',':
                    i += 1 
                    num2 = ""
                    
                    while i < len(input_string) and input_string[i].isdigit():
                        num2 += input_string[i]
                        i += 1
                    
                    if i < len(input_string) and input_string[i] == ')':
                        i += 1 
                        if num1.isdigit() and num2.isdigit():
                            result += int(num1) * int(num2)
                        continue
            
            # If disabled or the mul instruction is invalid, skip to the next character
            i += 1
        else:
            # Skip to the next character if no relevant instruction is found
            i += 1

    return result


corrupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
result = parse_muls(corrupted_memory)
print(result)

with open("Day 3\\input.txt", 'r') as f:
    s = str(f.read())

print(parse_muls(s))
print(parse_mul_do(s))