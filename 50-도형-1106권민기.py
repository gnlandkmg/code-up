import turtle

pen = turtle.Turtle()

pen.shape('turtle')

pen.color("blue")

pen.fillcolor("yellow")

pen.begin_fill()
for i in range(0,3):
    pen.forward(100)
    pen.left(120)
pen.end_fill()


pen.up()
pen.forward(130)
pen.down()
for i in range(0,4):
    pen.forward(100)
    pen.left(90)

pen.up()
pen.backward(330)
pen.down()
for i in range(0,6):
    pen.forward(100)
    pen.left(60)
turtle.done()
