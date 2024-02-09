# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100

#array initialization
arr = [0] 

#loop for inserting values to the pre nitialized array
for num in range(1 , 101): 
    arr.append(num)

#ibbonacci array initialization
new_fibbonacci_arr = [0] 
ans = 0

#loop for inserting the values to the fibonnacci sequence array
for num in range(1,101):
    new_fibbonacci_arr.append(num)
    ans += arr[num]
    new_fibbonacci_arr.append(ans)
    
print(new_fibbonacci_arr)
