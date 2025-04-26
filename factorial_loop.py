def factorial_loop(n):
    #Calculates factorial using iteration
    #Process: Multiplies numbers from 1 up to n
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Test
print("The answer is: ",factorial_loop(5))   # Output: 120
print("The answer is: ",factorial_loop(0))   # Output: 1