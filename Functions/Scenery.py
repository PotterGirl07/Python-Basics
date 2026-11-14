import turtle

paper = turtle.Screen()
pen = turtle.Turtle()
pen.speed(100)

paper.bgcolor("#0E0C48")

def rect(w, h):
    pen.begin_fill()
    for i in range(2):
        pen.forward(w)
        pen.right(90)
        pen.forward(h)
        pen.right(90)
    pen.end_fill()

def tri(side):
    pen.begin_fill()
    for i in range(3):
        pen.forward(side)
        pen.left(120)
    pen.end_fill()

def jump(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

pen.color("#8C845D")
jump(-1000,-200)
rect(2000, 300)
jump(0,-200)
pen.color("#CBBD76")
tri(300)
jump(-100,100)
pen.begin_fill()
pen.color("#f8ebd2")
pen.circle(70)
pen.end_fill()
jump(-50, 150)
pen.begin_fill()
pen.color("#0E0C48")
pen.circle(75)
pen.end_fill()


turtle.mainloop()