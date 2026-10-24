subs=("English", "Science", "History", "Math")
print(subs)
print("Printing index 0")
print(subs[0])
print("Printing index -2")
print(subs[-2])

print(" ")

print("Your choices: Harry, Hermione, Ron")
names=["Harry", "Hermione", "Ron"]
for i in range(3):
    name=input("Enter a name: ")
    names.append(name)
print("Printing index -2 of your order of names")
print(names[-2])