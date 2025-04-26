def sum_list_elements(data):
    #Returns the sum of all numbers in a list
    #process: It start with 0 and adds each number one by one 
    total = 0
    for num in data:
        total += num
    return total

# Test
print("The sum of all the elements is: ",sum_list_elements([1, 2, 3]))      # Output: 6
print("The sum of all the elements is: ",sum_list_elements([10, -5, 7]))   # Output: 12