import turtle

colors = ["red", "purple", "blue", "green", "orange", "yellow"]
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0) # Fastest speed

for x in range(100):
    t.pencolor(colors[x % 6]) # Rotate through colors
    t.width(x // 25 + 1)
    t.forward(x)
    t.left(59)