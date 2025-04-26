def factorial_recursive(n):
    #Calculates factorial using recursion
    #Process: The function calls itself with n-1 until it reaches 1
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

# Test
print("The answer is: ",factorial_recursive(5))   # Output: 120
print("The answer is: ",factorial_recursive(3))   # Output: 6