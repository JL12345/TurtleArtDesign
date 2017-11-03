import turtle
bob=turtle.Turtle()
from flower import*
bob.speed(0)
turtle.bgcolor("black")

flower(bob,"yellow",-250,200)
flower(bob,"green",0,200)
flower(bob,"blue",250,200)
flower(bob,"red",-150,-200)
flower(bob,"brown",150,-200)
flower(bob,"white",0,-25)

turtle.done()

