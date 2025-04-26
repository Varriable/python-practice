def check_even_odd(number):
    #Returns 'Even' or 'Odd' based on input number
    #Process: Even numbers divide by 2 with no remainder
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test
print("The numer is: ",check_even_odd(8))    # Output: Even
print("The numer is: ",check_even_odd(13))   # Output: Odd