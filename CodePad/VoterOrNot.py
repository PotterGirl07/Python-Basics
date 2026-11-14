# Originial Version
age=18
if age>=18:
    print("You can vote since you're over the age limit for voting.")
else:
    print("You can't vote, you're not of age yet.")


# Modified Version W/ Loops
while True:
    age = int(input("Enter the age: "))
    citizen = input("Are you a citizen? (True/False): ")

    if citizen != "True" and citizen != "False":
        print("Invalid")
        continue

    if age >= 18 and citizen == "True":
        print("You can vote!")
    elif citizen == "False":
        print("You can't vote because you are not a citizen.")
    else:
        print("You can't vote, you're not of age yet.")

    