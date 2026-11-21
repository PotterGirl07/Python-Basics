import pgzrun #python game zero run
WIDTH = 500
HEIGHT = 500

x = 100
y = 100

x2 = 100
y2 = 130

def draw():
    global screen
    screen.fill("Yellow")

    screen.draw.filled_rect(
        Rect((x,y),(30,30)),"Blue")

    screen.draw.filled_rect(
        Rect((x2,y2),(30,30)),"Red")

def update():
    global x, y, x2, y2

    if keyboard.down:
        y = y + 10
        y2 = y2 + 10

    if keyboard.up:
        y = y - 10
        y2 = y2 - 10

    if keyboard.right:
        x = x + 10
        x2 = x2 + 10

    if keyboard.left:
        x = x - 10
        x2 = x2 - 10

pgzrun.go()