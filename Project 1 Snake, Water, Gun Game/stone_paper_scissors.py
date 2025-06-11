
import random

list = {-1 : "Stone",
         0 : "Paper",
         1 : "Scissors"
         }
# paper = 0
# scissors = 1


choices = [1,0,-1]
computer = random.choice(choices)

print("Welcome to Stone-Paper-Scissor Game ! ")
print("Enter your choice: \nStone = -1\nPapers = 0\nScissors = 1")
user_choice = int(input("Enter your choice:"))

'''
if(computer == user_choice):
    print("It's a tie!")
elif(user_choice == 0 and computer == -1):
    print("You win!\nyou chose Paper and computer chose Stone")
elif(user_choice == 1 and computer == 0):
    print("You win!\nyou chose Scissors and computer chose Paper")
elif(user_choice == -1 and computer == 1):
    print("You win!\nyou chose Stone and computer chose Scissors")
else:
    print(f"you lose! :(\nComputer chose {computer} and you chose {user_choice}")

'''

if(computer == user_choice):
    print("It's a tie!")
elif(user_choice- computer == 1 and user_choice- computer == -2):
    print(f"you win!\nyou chose {list[user_choice]} and computer chose {list[computer]}")
else:
    print(f"you lose! :(\nComputer chose {list[computer]} and you chose {list[user_choice]}")

'''
lets consider the
'''

'''
*** win ***
 0  -1    -1  1
 1   0     1  1
-1   1     0 -2
*** lose ***
 0  1      1 -1
 1 -1      0  2
-1  0     -1 -1

'''








