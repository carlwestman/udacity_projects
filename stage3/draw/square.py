import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.width(10)
    for i in range(0,4):
        brad.forward(100)
        brad.right(90)

    angie = turtle.Turtle()
    angie.circle(100)
    angie.color("blue")


    peter = turtle.Turtle()
    peter.shape("arrow")
    peter.color("white")
    peter.width(5)
    for i in range(0,3):
        peter.back(100)
        peter.right(240)

    window.exitonclick()

# draw_shapes()


def draw_flower():
    window = turtle.Screen()

    stem = turtle.Turtle()
    stem.shape("classic")
    stem.right(90)
    stem.color("green")
    stem.width(4)
    stem.forward(300)
    stem.right(180)
    stem.forward(300)

    leaf1 = turtle.Turtle()
    leaf1.color("green")
    leaf1.up()
    leaf1.right(90)
    leaf1.forward(270)
    leaf1.right(90)
    leaf1.forward(20)
    leaf1.shape("circle")
    leaf1.shapesize(5,1,0)
    leaf1.fill("green")
    leaf1.settiltangle(45)

    leaf2 = turtle.Turtle()
    leaf2.color("green")
    leaf2.up()
    leaf2.right(90)
    leaf2.forward(270)
    leaf2.left(90)
    leaf2.forward(20)
    leaf2.shape("circle")
    leaf2.shapesize(5,1,0)
    leaf2.fill("green")
    leaf2.settiltangle(-45)

    flower = turtle.Turtle()
    flower.color("red")
    flower.speed(20)

    for i in range(0, 180):
        flower.forward(100)
        flower.right(179)
        flower.forward(100)

    window.exitonclick()

draw_flower()


