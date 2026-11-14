#default arguement
#when you call a function and it has no arguement
#then it shouldn't crashout


def greet(name="user"):
    print(f"Hello {name}!")

greet()
greet("Aashra")
