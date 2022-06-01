import turtle
from turtle import Turtle,Screen
import random
colorlist=[(248, 246, 236), (237, 250, 244), (251, 239, 248), (236, 243, 250), (233, 222, 92), (211, 158, 105), (116, 177, 210), (226, 57, 131), (181, 78, 33), (210, 135, 174), (41, 103, 161), (12, 21, 62), (184, 46, 111), (186, 164, 23), (43, 182, 112), (122, 187, 155), (25, 32, 158), (173, 16, 67), (234, 164, 199), (229, 75, 43), (22, 179, 205), (11, 41, 23), (49, 126, 73), (146, 218, 196), (51, 21, 11), (227, 220, 10), (106, 95, 206), (133, 215, 229), (175, 177, 227), (59, 16, 31), (237, 170, 158), (19, 92, 47), (158, 26, 17), (10, 84, 100), (44, 39, 243), (97, 73, 13), (249, 11, 26)]
tur = Turtle()
turtle.colormode(255)
screen=Screen()
tur.speed(30)
tang=-200
bang=-200
for i in range(10):
    tur.penup()
    tur.goto(bang,tang)
    tur.pendown()

    for j in range(10):
        rand=random.choice(colorlist)
        tur.pencolor(rand)
        tur.fillcolor(rand)
        tur.begin_fill()
        tur.circle(10)
        tur.end_fill()
        tur.penup()
        tur.forward(50)
        tur.pendown()
        tang+=3

screen.exitonclick()