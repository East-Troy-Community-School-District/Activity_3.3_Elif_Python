'''
Draw Shapes
Pawelski
1/27/2025

Instructions:
1.  Predict what this program will do. Check your prediction by
    running the program and entering a variety of shapes.
2.  Why does the program say "RECTANGLE" is an unrecognized shape?
3.  Add another elif statement to the program so that it draws a
    circle when the user enters "circle".
'''

import turtle

t = turtle.Turtle()
t.hideturtle()

shape = turtle.textinput("Shape", "Would you like to see a rectangle, square, or triangle?")

if shape == "rectangle":
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
elif shape == "square":
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
elif shape == "triangle":
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
# Add your code here!
else:
    t.write("Please enter a shape I know.", align="center", font=("Comic Sans MS", 40))

turtle.mainloop()