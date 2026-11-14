# It will not show any error on the user's screen 
# Even if they enter a word
# Leading to bad user experience

# So, show an error message

#Numerical Test

try:
    age = int(input("Enter your age: "))
    decade = age + 10
    print(f"After a decade, 10 years, you will be {decade} old.")
except ValueError:
    print("Invalid Number! Only use integers(numbers), not words.")


try:
    num1 = 10
    num2 = 0
    print(num1/num2)
except ZeroDivisionError:
    print("UNDEFINED!")