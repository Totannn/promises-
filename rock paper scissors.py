print("lets [lay rock paper scissors")
import random
def game():
     user = input("input your choice? 'r' for rock, 's' for scossors,'p for papaer'")
     user = user.lower()

     computer = random.choice(['r','s','p'])
     if user == computer:
          return"it is a draw".format(computer)
     if is_win(user,computer):
          return "you have chosen {} and computer has chosen  {}. you won!".format(user,computer)
     return "you have chosen {} and computer has chosen  {}. you lost!".format(user,computer)
def is_win(player,opponent):
     if (player=="r" and opponent=="s") or (player=="r" and opponent=="s") or (player=="s" and opponent=="p"):
          return True
     return False

print(game())