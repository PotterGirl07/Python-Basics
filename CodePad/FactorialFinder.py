num=int(input("Enter a number: "))
product=1
for i in range(1,num+1):
    product*=i
print("A factorial is a # multiplied by all #'s before it. The factorial of your # is:",product)

num=int(input("Enter another number: "))
product=1
i=1
while i<=num:
    product*=i
    i+=1
print("A factorial is a # multiplied by all #'s before it. The factorial of your # is:",product)