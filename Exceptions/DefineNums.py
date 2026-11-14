for i in range(100):
    try:
        num = float(input("Enter a number: "))

        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        elif num == 0:
            print("Zero")

        if num != 0:
            if num % 1 != 0:
                print("Decimal")
            else:
                if num % 2 == 0:
                    print("Even")
                else:
                    print("Odd")

                if num >= 0 and int(num ** 0.5) ** 2 == num:
                    print("Perfect Square")
                else:
                    print("Not A Perfect Square")

    except ValueError:
        print("Invalid input! Please enter a number, not a word.")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")