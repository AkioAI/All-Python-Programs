import turtle

turtle.color("black","Red")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("Black","Blue")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("Black","Yellow")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.end_fill()

turtle.exitonclick()
