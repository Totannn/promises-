import random


         



def roll_dice():
     rolldice = random.randint(1,6)
     return rolldice

NAME = input("PLEASE INSERT YOUR NAME")
print("ARE YOU READY TO ROLL YOUR DICE", NAME)
ANSWER = input("yes or no")
if ANSWER == "yes":
   print(roll_dice())
elif ANSWER =="no":
   print("get out")


