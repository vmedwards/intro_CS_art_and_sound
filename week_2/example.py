import turtle

turtle.forward(100)
turtle.left(90)
turtle.forward(50)

cur_pos = turtle.pos()
print("CUR POS: ", cur_pos)

x_coordinate = turtle.xcor()
y_coordinate = turtle.ycor()
print("X: ", x_coordinate)
print("Y: " + str(y_coordinate))


t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.forward(100)
t2.right(90)
t2.forward(100)
t1.forward(100)
t1.left(90)
t1.forward(100)

turtle.exitonclick()


turtle.exitonclick()


