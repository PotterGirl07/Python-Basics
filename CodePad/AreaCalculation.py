#square
side=int(input("Enter a side of a square: "))
area=side*side
print(f"Area of a square with a side of {side}in is {area}in sq.")

#rectangle
length=int(input("Enter the length of a rectangle: "))
width=int(input("Enter the width of a rectangle: "))
area=length*width
print(f"Area of a rectangle with a length of {length}in and a width of {width}in is {area}in sq.")

#triangle
#area=b*h*0.5
base=int(input("Enter the base of a triangle: "))
height=int(input("Enter the height of a triangle: "))
area=base*height*0.5
print(f"Area of a triangle with a base of {base}in and a height of {height}in is {area}in sq.")

#circle=pi*r*r
radius=int(input("Enter the radius of a circle: "))
area=3.14*radius*radius
print(f"Area of a circle with a side of {radius}in is {area}in sq.")