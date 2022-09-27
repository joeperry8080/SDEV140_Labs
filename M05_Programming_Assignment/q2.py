# import the random and datetime libraries to create a true random number for use
import random
import datetime

max_rand = 100

def my_game():
    flag = 0
    u_try = 1
    # randomize the seed then get a random int based on the datetime
    current_date = datetime.datetime.now()
    random.seed(int(current_date.strftime("%Y%m%d%H%M%S")))
    rand = random.randint(0,max_rand)

    while flag < 3:
        while flag < 2:  
            u_num = int(input("Enter a number between 1 and 100: "))

            if u_num > rand:
                print("Too high, try again.")
                rand = rand
                flag = 0
                u_try = u_try + 1
            elif u_num < rand:
                print("Too low, try again.")
                rand = rand
                flag = 0
                u_try = u_try + 1
            elif u_num == rand:
                print("Congratulations! You did it in " + str(u_try) + " tries.")
                v_try = input("\nDo you want to try again? (y/n) ")
                if v_try == 'y':
                    flag = 1
                    rand = random.randint(0,max_rand)
                if v_try == 'n':
                    flag = 3
                else:
                    flag = 3        
            # this is here to catch anything else and prevent an infinite loop
            else:
                flag = 3
    
    return 0

my_game()