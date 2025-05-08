import random
def game():


    print("****************************************************************")
    print("Welcome to Stone-Paper-Scissor Game ! ")
    print("Enter your choice: \nStone = -1\nPapers = 0\nScissors = 1")
    global score
    score = 0
    for i in range(0,11):
        list = {-1 : "Stone",
                0 : "Paper",
                1 : "Scissors"
                }

        choices = [1,0,-1]
        computer = random.choice(choices)
        print("****************************************************************")
        user_choice = int(input("Enter your choice:"))
        if user_choice not in [-1,0,1]:
            print("*** invaild choices ***\n#### YOU LOSE ONE CHANCE ####\nPlease choose between [1,0,-1]")
        elif(computer == user_choice):
            print("It's a tie!")
        elif((user_choice == 0 and computer == -1) or (user_choice == 1 and computer == 0) or (user_choice == -1 and computer == 1)):
            print(f"You win!\nyou chose {user_choice} and computer chose {computer}")
            score += 1
        else:
            print(f"you lose! :(\nComputer chose {computer} and you chose {user_choice}")
            

    with open("HI-SCORE.txt", "r") as f:
        num = f.read()
        hi_score = int(num)
        if score > hi_score:
            print(f"Congratulations! You have reached the new high score of {score}.")
            with open("HI-SCORE.txt", "w") as r:
                r.write(str(score))


game()