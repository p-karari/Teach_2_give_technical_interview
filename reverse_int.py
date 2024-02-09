# question 5
# Write a program that takes an integer as input and returns an integer with reversed digit 
# ordering

raw_input = int(input("Enter an integer: "))



#  function that will Convert the integer to a string, reverse it, and convert it back to an integer
def reverse_integer(n):
    #slicing with a step value of -1, returns the string in the reverse order
    reversed_str = str(n)[::-1]
    reversed_int = int(reversed_str)
    return reversed_int

result = reverse_integer(raw_input)

print(result)