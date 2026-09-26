import random

bscore = 0
yscore = 0

for i in range(3):
    print("Welcome to the  Ultimate Game of Rock, Paper, or Scissors")
    you = input("Pick one: rock, paper, or scissors: ")
    if you!="rock" and you!="paper" and you!="scissors":
        print("Invalid input!")
        continue

    else:
        num = random.randint(1,3)
        if num==1:
            bot="rock"
        elif num==2:
            bot="paper"
        elif num==3:
            bot="scissors"
        print(f"You chose: {you}")
        print(f"Computer chose: {bot}")

        #Scenario: tie
        if bot==you:
            print("It's a draw!!")

        #Scenario: you win
        elif (you=="rock" and bot=="scissors") or (you=="paper" and bot=="rock") or (you=="scissors" and bot=="paper"):
            print("You won!!!!")
            yscore+=1

        #Scenario: you lose
        else:
            print("You lose, Bot wins! YOU SUCKKKKKK!!!!!!")
            bscore+=1
    print("~"*50)
print(f"Your score: {yscore}")
print(f"Bot's score: {bscore}")
