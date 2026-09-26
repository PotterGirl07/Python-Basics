
#1
for i in range(3):
    ques1 = input("Who served as the first president of the USA? ").lower()
    ans1 = "George Washington".lower()

    if ques1==ans1:
        print("You got it, smarty-pants. But this was only the first question.")
        break
    else:
        print("No, that's wrong.")

if ques1!=ans1:
    print("Good effort! But the answer was George Washington.")


#2
for i in range(3):
    ques1 = input("What is the only edible thing that never spoils, if stored correctly? ").lower()
    ans1 = "Honey".lower()

    if ques1==ans1:
        print("Cool! You guessed it!")
        break
    else:
        print("Oh no! Wrong!")

if ques1!=ans1:
    print("Your tries are up! The answer was honey.")

#3
for i in range(2):
    ques1 = input("What is the only planet in our solar system that rotates clockwise?(You only get 2 tries for this one): ").lower()
    ans1 = "Venus".lower()

    if ques1==ans1:
        print("You got it! Good job!")
        break
    else:
        print("No...")

if ques1!=ans1:
    print("Nice try, but no! The correct answer was Venus.")

#4
for i in range(3):
    ques1 = input("What is the only mammal that lays eggs? ").lower()
    ans1 = "Platypus".lower()

    if ques1==ans1:
        print("Correct! How'd you know!!??")
        break
    else:
        print("Wrong! But don't give up yet!")

if ques1!=ans1:
    print("Good try, but the answer was a platypus. Who knew?")


#5
for i in range(3):
    ques1 = input("What is the only letter that does not appear in the periodic table's element symbols? ").lower()
    ans1 = "J".lower()

    if ques1==ans1:
        print("You got it! Nice!")
        break
    else:
        print("Nope!")

if ques1!=ans1:
    print("You had 26 letters to choose from, and you still missed it! The answer was J.")


#6
for i in range(3):
    ques1 = input("What nation has the most time zones and how many does it have? Answer like this: Country(# of time zones) : ").lower()
    ans1 = "France(12)".lower()

    if ques1==ans1:
        print("Bingo! Right on the dot.")
        break
    else:
        print("Nah, think Europe.")

if ques1!=ans1:
    print("Wrong times three! The correct answer was France, with 12 time zones.")


#7
for i in range(3):
    ques1 = input("What structure gets slightly taller during hot weather? Start your answer with the word 'The' : ").lower()
    ans1 = "The Eiffel Tower".lower()

    if ques1==ans1:
        print("Nailed it. Just a few to go!")
        break
    else:
        print("Wrong answer. Think famous.")

if ques1!=ans1:
    print("No more guesses! The answer was Eiffel Tower. Just a few questions to go!")


#8
for i in range(3):
    ques1 = input("Which animal has rectangular pupils? ").lower()
    ans1 = "Goat".lower()

    if ques1==ans1:
        print("Yep! That's it! Almost to the end.")
        break
    else:
        print("Nope! Not quite!")

if ques1!=ans1:
    print("Couldn't get it? That's okay! The answer was a goat. You're almost at the end!")


#9
for i in range(3):
    ques1 = input("Which living thing has blue blood, three hearts and nine brains? ").lower()
    ans1 = "octopus".lower()

    if ques1==ans1:
        print("Yeahhh! That's amazing.")
        break
    else:
        print("You got it ....           wrong.")

if ques1!=ans1:
    print("The correct answer was an octopus. Cool fact, isn't it?! Just one more question left!")


#10
for i in range(3):
    ques1 = input("Final challenge: Can you spell the famous 45-letter English word? Good luck! Try here: ").lower()
    ans1 = "pneumonoultramicroscopicsilicovolcanoconiosis".lower()

    if ques1==ans1:
        print("You got it! Wow! Look at you cook. Quiz over!")
        break
    else:
        print("I knew you'd mess up.")

if ques1!=ans1:
    print("I knew you'd never get it, it was: pneumonoultramicroscopicsilicovolcanoconiosis.")

#Fact
fact = input("Want to know a fun fact? ").lower()
if fact=="Yes".lower():
    print("The longest known English word is a chemical name with an unbelievable 189,819 letters—it would take about 3.5 hours to say! 🤯")
else:
    print("Well, that's too bad, I'm going to tell you anyway.")
    print("The longest known English word is a chemical name with an unbelievable 189,819 letters—it would take about 3.5 hours to say! 🤯")