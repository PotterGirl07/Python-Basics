#creates an empty set
pwset=set()
pwlist=[]
print("Welcome to Your Password Vault")
while True:
    print("1. Create a password")
    print("2. Login")
    print("3. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        psw1=input("Enter password: ")
        if psw1 in pwset:
            print("Unavailable. This has already been used, please enter a new one. ")
            continue
        else:
            psw2=input("Re-enter password: ")
            if psw1==psw2:
                print("New Password Successfully Stored!")
                pwset.add(psw1)
                pwlist.append(psw1)
    elif choice=="2":
        psw=input("Enter your password: ")
        if psw==pwlist[-1]:
            print("Login Successful!")
        else:
            print("Wrong password. Please retry.")
            continue
    elif choice=="3":
        print("Bye! See you soon.")
        break
    else:
        print("Invalid choice.")
