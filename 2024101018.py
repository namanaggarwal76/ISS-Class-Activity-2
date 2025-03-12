def is_narc(n): #fix1
    """Check if a number is narc."""
    num_str = str(n) #fix2
    num_digits = len(num_str) #fix3
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str) #fix4
    
    return sum_of_powers == n

def print_narcis_numbers(start, end): #fix5
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1): #fix6
        if is_narc(num): #fix7 and fix8
            print(num)

print_narcis_numbers(1000, 5000)  #fix9
