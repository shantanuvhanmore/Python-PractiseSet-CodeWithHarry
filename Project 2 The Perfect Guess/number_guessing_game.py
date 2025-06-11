from random import randint
num = randint(1,100)
n = 0
print("****************************************")
print("WELCOME TO THE NUMBER GUESSING GAME !!")
print("****************************************")
print("Guess a number between 1 - 100 :")
count=0
while n != num:
    n = int(input("----> "))
    count += 1
    if n == num:
        break
    elif(n > num ):
        print("guess lower !!")
    else:
        print("guess higher !!")

print("****************************************************")
print(f"congrats Buddy !! your guess was right ----> its {n}\nyou Guess this in {count} chances !!")
print("****************************************************")