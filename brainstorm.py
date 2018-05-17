import turtle

def draw_square(name):
    name.shape("turtle")
    name.color("yellow")
    name.speed(5)
    cont = 0

    while(cont < 4):
        name.forward(100)
        name.right(90)
        cont = cont + 1

def draw_circle(name):
    name.shape("arrow")
    name.color("blue")
    name.circle(50)

def draw_triangle(name, num_aresta):
    name.shape("turtle")
    name.color("purple")
    name.speed(5)
    cont = 0

    while(cont < num_aresta):
        name.forward(100)
        name.right(120)
        cont = cont + 1

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    angie = turtle.Turtle()
    donatelo = turtle.Turtle()

    draw_square(brad)
    draw_circle(angie)
    draw_triangle(donatelo, 3)

    window.exitonclick()

def draw_final_art():
    window = turtle.Screen()
    window.bgcolor("red")

    raphael = turtle.Turtle()

    for i in range (1, 37):
        draw_square(raphael)
        raphael.right(10)

    window.exitonclick()

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    leonardo = turtle.Turtle()

    for i in range (1,37):
        draw_triangle(leonardo, 2)
        leonardo.right(50)

    window.exitonclick()

draw_flower()
