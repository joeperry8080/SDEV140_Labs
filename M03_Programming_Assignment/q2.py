#Write a program that writes a series of random numbers to a file and displays all #the numbers to the console. 
#Each random number should be in the range of 1 through 500. 
#The application should let the user specify how many random numbers the file will hold.

import random
import datetime

current_date = datetime.datetime.now()

def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

#randomize the seed
random.seed(int(current_date.strftime("%Y%m%d%H%M%S")))


#f = open("./M03_Programming_Assignment/output.txt", "wt")
f = open("output.txt", "wt")

rangeNum = int(input("How many random numbers do you want to generate?"))

for i in range(rangeNum):
    
    flag = random.randint(0,500)
    print(flag)

    if flag < 100:
        num = random.randint(0,5000)
    else:
        num = random.random()

    f.write(str(num) + "\n")

f.close()
