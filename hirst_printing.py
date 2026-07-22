import colorgram as c
color=c.extract(r"C:\Users\shali\Downloads\hirst_lsd__2000.jpg",50)

list_of_color=[]
for colours in color:
    t=tuple(colours.rgb)
    list_of_color.append(t)

print(list_of_color)
import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)

tim = Turtle()
tim.penup()
tim.speed("fastest")
# this is the extracted colours from the image which will also display in output terminal
list_color = [(241, 236, 231), (176, 12, 63), (9, 111, 157), (217, 172, 15), (245, 223, 231), (240, 206, 76), (185, 72, 36), (215, 165, 61), (221, 233, 229), (117, 175, 203), (215, 232, 239), (229, 67, 144), (15, 42, 99), (19, 121, 66), (5, 101, 68), (236, 160, 191), (141, 33, 27), (222, 85, 39), (167, 50, 83), (19, 40, 118), (23, 176, 194), (82, 26, 85), (50, 176, 158), (247, 197, 2), (3, 78, 51), (3, 98, 108), (98, 183, 151), (211, 130, 159), (213, 180, 176), (99, 126, 195), (151, 207, 215), (156, 209, 196), (181, 182, 215), (98, 23, 20)]

start_x = -200
start_y = -200

tim.goto(start_x, start_y)

for row in range(10):

    for dot in range(10):
        tim.dot(20, random.choice(list_color))
        tim.forward(50)

    start_y += 50
    tim.goto(start_x, start_y)

screen = Screen()
screen.exitonclick()
