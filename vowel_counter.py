# question 6: Count Vowels
# Write a program that counts the number of vowels in a sentencs

sentence = input("Enter sentence : ")
vowels = "aeiouAEIOU"

#count variable is for storing the count of vowels in the given sentence, initial value is 0
count = 0

#Loop for counting the vowels and incrementing the count variable depending of the number of vowels in the sentence
for char in sentence:
        if char in vowels:
            count += 1

print("Number of vowels : ", count)
