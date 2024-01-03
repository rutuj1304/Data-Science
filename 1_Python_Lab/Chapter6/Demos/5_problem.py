"""
random.randint(1,100)

guess the random number

"""
import random

random_num = random.randint(1, 100)

user_input = int(input("guess the random number:  "))

temp =1
while user_input > 0:
    if random_num > user_input:
        print("Entered number is too low, please guess it again")
        user_input = int(input("guess the random number:  "))
        temp +=1
    elif random_num < user_input:
        print("Entered number is too high, please guess it again")
        user_input = int(input("guess the random number:  "))
        temp+=1
    else:
        print("Congratualations!, You got it..")
        print("Total number of attempts: ",temp)
        break
        
        


