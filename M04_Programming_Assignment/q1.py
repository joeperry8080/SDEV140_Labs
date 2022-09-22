# display all the prime numbers within an interval
# prime numbers are greater than 1
#   prime number have no divisors other 1 or itself
uNum = int(input("Enter a number greater than 1: "))
numList = []
primeList = []

# create a loop to set a range based on user input
for num in range(1, uNum + 1):
   if num > 1:
       numList.append(num)
       
       for i in range(2, num):
           # if not prime, then break
           if (num % i) == 0:
               break
       else:
           primeList.append(num)

print("These are the prime numbers from your list: ")
print(primeList)           