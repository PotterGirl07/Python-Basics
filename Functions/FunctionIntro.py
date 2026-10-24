#function is a set of instructions
#they are put together in a code block
#they can be called/used as many times as needed
#Functions are of 2 types
    #Inbuilt ~ print, input, int, etc
    #can be called in another file
    #User-Definined ~ which are as follows
    #cannot be called in another file
#Function has 3 steps
    #Define & Call
#after creating, you can call it whenever in the same file - DRY

#1. Define
def BrushTeeth():
    print("1. Rinse your toothbrush")
    print("2. Put toothpaste on it")
    print("3. Brush your teeth")
    print("4. Wash your brush")
    print("5. Rinse your mouth thoroughly")

#2. Call
BrushTeeth()
#Makes code DRY
    #Don't Repeat Yourself
BrushTeeth()
    