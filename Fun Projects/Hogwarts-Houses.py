print("Which Hogwarts House Are You?\nTake this quiz to find out!")
print("~"*100)
g=0
r=0
s=0
h=0

print("Questions #1")
print("You find a mysterious door at Hogwarts. What do you do?")
print(" A. Open it immediately. I love an adventure!\n B. Look for clues and figure out what's behind it.\n C. Think about how opening it could benefit me.\n D. Ask your friends to come with you.")
ans1 = input("Enter your choice: A/B/C/D: ").upper()
if ans1=="A":
    g+=1
elif ans1=="B":
    r+=1
elif ans1=="C":
    s+=1
elif ans1=="D":
    h+=1
else:
    print("Invalid, you wasted your chance.")
print("Registered your choice.")


print("~"*100)


print("Question #2")
print("You are given a difficult puzzle. Your first thought is:")
print(" A. Let me carefully analyze every clue logically.\n B. How can I turn this into an advantage and sabotage others?\n C. Let's work through it together.\n D. Think first and keep trying, never give up.")
ans2=input("Enter your choice A/B/C/D: ").upper()
if ans2=="A":
    r+=1
elif ans2=="B":
    s+=1
elif ans2=="C":
    h+=1
elif ans2=="D":
    g+=1
else:
    print("Invalid! You missed your chance.")
print("Registered your choice!")


print("~"*100)


print("Question #3")
print("What would you want people to think of you as?")
print(" A. Being clever and creative\n B. Achieving something great\n C. Being loyal and dependable\n D. Being brave and everything else")
ans3=input("Enter your choice A/B/C/D: ").upper()
if ans3=="A":
    r+=1
elif ans3=="B":
    s+=1
elif ans3=="C":
    h+=1
elif ans3=="D":
    g+=1
else:
    print("Invalid! You missed your chance.")
print("Registered your choice!")


print("~"*100)


print("Question #4")
print("Your team is losing an important Quidditch match. What do you do?")
print(" A. Take a risky shot to turn the game around\n B. Look for a weakness in the other team and do illegal moves to win\n C. Encourage everyone to keep trying\n D. Come up with a new strategy")
ans4=input("Enter your choice A/B/C/D: ").upper()
if ans4=="A":
    g+=1
elif ans4=="B":
    s+=1
elif ans4=="C":
    h+=1
elif ans4=="D":
    r+=1
else:
    print("Invalid! You missed your chance.")
print("Registered your choice!")


print("~"*100)


print("Question #5")
print("Someone challenges you to a wand duel. How do you respond?")
print(" A. Try to negotiate instead\n B. Find a way to gain an advantage beforehand\n C. Accept without hesitation\n D. Study their fighting style first")
ans5=input("Enter your choice A/B/C/D: ").upper()
if ans5=="A":
    h+=1
elif ans5=="B":
    s+=1
elif ans5=="C":
    g+=1
elif ans5=="D":
    r+=1
else:
    print("Invalid! You missed your chance.")
print("Registered your choice!")


print("~"*100)


print("Question #6")
print("You get detention for something you didn't do. What do you do?")
print(" A. Figure out what evidence could prove your innocence\n B. Find a clever way to turn the situation in your favor\n C. Stand up for yourself and demand the truth\n D. Stay calm and explain what really happened")
ans6=input("Enter your choice A/B/C/D: ").upper()
if ans6=="A":
    r+=1
elif ans6=="B":
    s+=1
elif ans6=="C":
    g+=1
elif ans6=="D":
    h+=1
else:
    print("Invalid! You missed your chance.")
print("Registered your choice!")


print("~"*100)


print("Question #7")
print("Which room would you choose to spend an evening in?")
print(" A. A warm, cozy room filled with good company\n B. A mysterious hidden room that no one else knows about\n C. A huge room with a fireplace, music, snacks and friends with different activities(dangerous and mid)\n D. A library with friends and snacks, reading and having fun")
ans7=input("Enter your choice A/B/C/D: ").upper()
if ans7=="A":
    h+=1
elif ans7=="B":
    s+=1
elif ans7=="C":
    g+=1
elif ans7=="D":
    r+=1
else:
    print("Invalid! You missed your chance.")
print("Registered your choice!")


print("~"*100)


print("Question #8")
print("You have to make an important decision quickly. What do you trust?")
print(" A. What I think I will gain from\n B. My courage and instincts\n C. Logic and what I know\n D. My values and what feels fair")
ans8=input("Enter your choice A/B/C/D: ").upper()
if ans8=="A":
    s+=1
elif ans8=="B":
    g+=1
elif ans8=="C":
    r+=1
elif ans8=="D":
    h+=1
else:
    print("Invalid! You missed your chance.")
print("Registered your choice!")


print("~"*100)


print("Question #9")
print("You can instantly become excellent at one of these things. Which do you choose?")
print(" A. Learning and understanding anything\n B. Persuasion and getting what I want\n C. Helping and understanding people\n D. Being fearless and better than my current self")
ans9=input("Enter your choice A/B/C/D: ").upper()
if ans9=="A":
    r+=1
elif ans9=="B":
    s+=1
elif ans9=="C":
    h+=1
elif ans9=="D":
    g+=1
else:
    print("Invalid! You missed your chance.")
print("Registered your choice!")


print("~"*100)


print("Question #10")
print("If you could instantly remove one problem from your life, which would you choose?")
print(" A. Anything that gets in the way of my goals\n B. Hesitating when I should act\n C. Not knowing enough or having unanswered questions\n D. Conflict with people I care about")
ans10=input("Enter your choice A/B/C/D: ").upper()
if ans10=="A":
    s+=1
elif ans10=="B":
    g+=1
elif ans10=="C":
    r+=1
elif ans10=="D":
    h+=1
else:
    print("Invalid! You missed your chance. The quiz is over!")
print("Registered your choice! The quiz is over!")


print("~"*100)


print("So.... ready to find out what your Hogwarts house percentage is?")

print("Gryffindor🦁:", g/10*100, "%")
print("Ravenclaw🦅:", r/10*100, "%")
print("Slytherin🐍:", s/10*100, "%")
print("Hufflepuff🦡:", h/10*100, "%")

print("~"*100)

if g > r and g > s and g > h:
    print("You are a Gryffindor! 🦁")
elif r > g and r > s and r > h:
    print("You are a Ravenclaw! 🦅")
elif s > g and s > r and s > h:
    print("You are a Slytherin! 🐍")
elif h > g and h > r and h > s:
    print("You are a Hufflepuff! 🦡")
else:
    print("No clear winner, check the percentages above.")
