rep={
    "Aashra":100,
    "Lucas":99,
    "Brianna":92,
    "Valeria":96,
    "Lochlann": 87,
}

print("Score Checker")
print("Options: Aashra/Lucas/Brianna/Valeria/Lochlann")
name=input("Enter a name: ").capitalize()
if name in rep:
    print(f"Hello {name}")
    print(f"You have scored {rep[name]} in this term.")