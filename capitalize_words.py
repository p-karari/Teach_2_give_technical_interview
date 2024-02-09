# Question 4: Capitalize Words
# Write a program that accepts a string as input, capitalizes the first letter of each word in the 
# string, and then returns the result string.

words = input("Enter string: ")

words = words.split()

#new array for storing the new capitalized words
capitalized_words = []

#loop for capitalizing first letter of every word. The capitalize() function does just that
for word in words:
    word = word.capitalize()
    capitalized_words.append(word.capitalize())
    
#now joining the capitalized word array to print as a sentence  
print(' '.join(capitalized_words))
    
    
    


    