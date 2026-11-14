def AddNums(n1, n2):
    result = n1 + n2
    print(result)

def SubNums(n1, n2):
    result = n1 - n2
    print(result)

def MulNums(n1, n2):
    result = n1 * n2
    print(result)

def DivNums(n1, n2):
    result = n1 / n2
    print(result)

while True:
    try:
        op = int(input("Enter 1/2/3/4 for +,-,*,/ respectively: "))
        if op == 1:
            n1 = float(input("Enter a number: "))
            n2 = float(input("Enter a number: "))
            AddNums(n1, n2)
        elif op == 2:
            n1 = float(input("Enter a number: "))
            n2 = float(input("Enter a number: "))
            SubNums(n1, n2)
        elif op == 3:
            n1 = float(input("Enter a number: "))
            n2 = float(input("Enter a number: "))
            MulNums(n1, n2)
        elif op == 4:
            try:
                n1 = float(input("Enter a number: "))
                n2 = float(input("Enter a number: "))
                AddNums(n1, n2)
            except ZeroDivisionError:
                print("UNDEFINED!")

    except ValueError:
        print("Enter 1/2/3/4 for +,-,*,/ respectively ONLY: ")