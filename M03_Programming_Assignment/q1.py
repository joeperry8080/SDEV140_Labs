# Write a program that asks the user to enter a series of single-digit numbers with nothing separating them. 
# The program should display the sum of all the single-digit numbers in the string. 
# For example, if the user enters 2514, the method should return 12, which is the sum of 2, 5, 1, and 4. 

x = 0
v_nums = input("Enter a series of single-digit numbers:")

#print(v_nums)

for i in v_nums:
    #print(i)
    x += int(i)

print(x)

x = 0
