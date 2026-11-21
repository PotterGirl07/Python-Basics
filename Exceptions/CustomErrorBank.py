def bank(balance):
    if balance<0:
        raise ValueError
    else:
        print("You're good to go!")
try:
    bank(-12)
except ValueError:
    print("Your balance is less than 0!")

# bank(-12)