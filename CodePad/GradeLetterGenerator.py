#0-59=F
#60-69=D
#70-79=C
#80-89=B
#90-100=A

score=int(input("Enter your score percentage: "))
if score<=100 and score>=90:
    print("Your grade is an 'A'. Awesome job!")
elif score<=89 and score>=80:
    print("Your grade is a 'B'. Good job, but you could do better.")
elif score<=79 and score>=70:
    print("Your grade is a 'C'. Be better.")
elif score<=69 and score>=60:
    print("Your grade is a 'D'. You're almost to a failing grade, don't get there.")
elif score<=59:
    print("Really? An 'F'? YOU'RE FAILING!! Study harder!")
else:
    print("Your score is invalid, it can only be between 0-100.")