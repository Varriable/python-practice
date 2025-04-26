def sum_of_digits(number):
    #Returns the sum of all digits in a number
    #Process: Converts to a string to access each digit easily
    total = 0
    num_str = str(number)  
    for digit in num_str:
        total += int(digit)
    return total

# Test
print("The sum of the digits is: ",sum_of_digits(1234))    # Output: 10
print("The sum of the digits is: ",sum_of_digits(999))     # Output: 27

