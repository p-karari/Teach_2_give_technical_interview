# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.

#have to import the log base 2 function for later use in the programme
from math import log2

raw_input =  int(input("Enter an integer: "))

is_a_power = False
if raw_input <= 0:
    is_a_power = False

#if the result  of log2 of the provided integer value is an integer , it is a power of 2
if int(log2(raw_input)) == log2(raw_input):
    is_a_power = True

print(is_a_power)
