import turtle


screen = turtle.Screen()
screen.title("Animated Circle")
screen.bgcolor("white")
screen.setup(width=600, height=600)


circle = turtle.Turtle()
circle.shape("circle")
circle.color("blue")
circle.penup()
circle.speed(0)


dx = 4
dy = 4

def animate():
    global dx, dy
    
    
    x = circle.xcor() + dx
    y = circle.ycor() + dy
    circle.goto(x, y)
    
    
    if x > 280 or x < -280:
        dx *= -1
    if y > 280 or y < -280:
        dy *= -1
    
    
    screen.ontimer(animate, 20)


animate()


screen.mainloop()