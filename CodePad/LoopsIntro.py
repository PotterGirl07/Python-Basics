#INTRODUCTION TO LOOPS
#while loop
print("While Loop:")
count=1
while count<3:
    print("Hey!")
    count=count+1
#for loop
print("For Loop:")
for count in range(2):
    print("Hey!")

#USE OF LOOPS
#While Loop
print("")
print("")
print("While Loop: Repetition")
counting=1
while counting<=3:
    print(f"Mic testing {counting}")
    counting+=1
print(" ")

print("While Loop: Sum 1~10")
counting=1
total=0
while counting<=10:
    total+=counting
    counting+=1
print(total)
print(" ")

print("While Loop: Countdown 3~1")
counting=3
while counting>=1:
    print(counting)
    counting-=1
print(" ")

print("While Loop: 2 Times Table")
count=2
while count<=10:
    print(count)
    count+=2

#For Loop
#count from 1-10
print("")
print("")
for c in range(1,4):
    print(f"Mic Testing {c}")

#2's times table
for num in range(2,12,2):
    print(num)