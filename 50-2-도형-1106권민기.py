import turtle

pen = turtle.Turtle()

pen.shape('turtle')

for i in range(0,4):
    pen.forward(100)
    pen.left(90)
pen.up()
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.down()
for i in range(0,3):
    pen.forward(100)
    pen.left(120)
