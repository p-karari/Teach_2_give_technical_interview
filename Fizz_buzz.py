# Question 1: FizzBuzz
# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for 
# multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print 
# "FizzBuzz".

#variable initialization
i = 1 
while i <= 100:
    if (i % 3 == 0) and (i % 5 != 0):
        x = "Fizz"
    elif (i % 5 == 0) and (i % 3 != 0):
        x = "Buzz"
    elif (i % 5 == 0) and (i % 3 == 0):
        x = "FizzBuzz"
    else :
        x = ""
    print(i , x)
    
    i +=1
