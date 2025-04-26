def reverse_string(input_string):
    #Reversing a string
    #Process: Builds new string by adding characters in reverse order
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

# Test
print("The reversed string is: ",reverse_string("Ramadhan")) # Output: nahdamaR
print("The reversed string is: ",reverse_string("python"))   # Output: nohtyp