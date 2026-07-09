#Python Project-Guessing Game
print('''-----GUESSING GAME-----
-----------------------------------------------------------
Welcome to the guessing game!!! This is a game, which will
try to bring out your hidden telepathic powers.Please read the instructions to understand the game.
-----INSTRUCTIONS-----
1) You can choose from three difficulties :-
   Noob : 1-5
   Pro : 1-10
   Hacker : 1-20
2) Each level has a range corresponding to it's difficulty. A number will be picked up in that range (including the start and end values). Try to guess that number. 
3) Your score will be displayed after each attempt. The score will be the number of attempts made. Higher the score means, it took more number of attempts to guess. Try for a score of 1.
4) You can choose to continue after finishing one round.
5) Each level has its number of attempts. The 1st one has 4 attempts. The second one has 8 attempts. The third one has 12 attempts.''')

import random #Random module imported for picking a number in the ranges.
def Noob(): #Function for level 1.
    score=0
    num=random.randint(1,5)
    for i in range(0,4):
        guess=int(input("Enter your guess:"))
        score+=1 
        if guess==num:
            print("CORRECT!!! Congratulations.")
            break
        else:
            print("Wrong guess!!! Your score currently :",score)
    else:
        print("The number was",num,". However, very nice of you for trying. Better luck next time.")
        
def Pro(): #Function for level 2.
    score1=0
    num1=random.randint(1,10)
    for j in range(0,8):
        guess1=int(input("Enter your guess:"))
        score1+=1
        if guess1==num1:
            print("CORRECT!!! Congratulations.")
            break
        else:
            print("Wrong guess!!! Your score currently :",score1)
    else:
        print("The number was",num1,". However, very nice of you for trying. Better luck next time.")
        
def Hacker(): #Function for level 3.
    score2=0
    num2=random.randint(1,20)
    for k in range(0,12):
        guess2=int(input("Enter your guess:"))
        score2+=1 
        if guess2==num2:
            print("CORRECT!!! Congratulations.")
            break
        else:
            print("Wrong guess!!! Your score currently :",score2)
    else:
        print("The number was",num2,". However, very nice of you for trying. Better luck next time.")

while True:
    choice=input("Do you wish to continue? Y/N:")
    if choice=="Y":
        difficulty=input("Choose N for Noob, P for Pro, or H for Hacker:")
        if difficulty=="N":
            Noob() #Function call for level 1.
        elif difficulty=="P":
            Pro() #Function call for level 2.
        elif difficulty=="H":
            Hacker() #Function call for level 3.
    else:
        print("Exited successfully!!!")
        break
        



