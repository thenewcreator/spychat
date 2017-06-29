#import the modules of the turtle
import turtle
colors = ['red','purple','blue','green','orange','yellow']
#defines the colours for the figure to be made

t = turtle.Pen()   #this is used for drawing the logo

turtle.bgcolor('black')   #defines the bakground colour

for x in range(50):
    t.pencolor(colors[x%6])  #defines the directions for drawing the logo
    t.width(x/80)
    t.forward(x)
    t.left(59)
t.backward(60)
t.write("Welcome to the world of ...",align='right', font=("Comic-Sans", 18, "normal",))  #text to be written
t.write("   UNKNOWNS!",align='left', font=("Comic-Sans", 18, "normal",))
turtle.mainloop() #stop the variable t i.e turtle.pen
