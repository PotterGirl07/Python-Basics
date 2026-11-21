def regv(age):
    if age<18:
        raise ValueError
    else:
        print("Registration Successful!")

try:
    regv(16)
except ValueError:
    print(f"Invalid input.")