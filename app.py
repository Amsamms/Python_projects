# import turtle
import turtle
# setting playing screen
wind = turtle.Screen() # initialize screen
wind.title('ping pong by Ahmed Sabri')
wind.bgcolor('black') # set backgroound color
wind.setup(width=800, height=600)
wind.tracer(0) # stops the windows from updating automatically
# madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0) # to not lag whiole moving
madrab1.shape('square')
madrab1.color('blue')
madrab1.penup()  # to not draw traces after moving
madrab1.shapesize(stretch_wid=5,stretch_len=1)
madrab1.goto(-350, 0)
# madrab2
madrab2 = turtle.Turtle() # initializa turtle object
madrab2.speed(0) # set the speed of animation
madrab2.shape('square') # set the shape of the object
madrab2.color('red') # set the color of the shape
madrab2.penup()  # stop the object from drawing lines
madrab2.shapesize(stretch_wid=5,stretch_len=1) # stretches the shape
madrab2.goto(-350, 150) # set the position of the object
# ball
ball = turtle.Turtle()
ball.speed(0) # to not lag whiole moving
ball.shape('square')
ball.color('white')
ball.penup()  # to not draw traces after moving
madrab1.goto(350, 0)
ball.dx = 0.5 # every time the ball is moving, x will be increased 2 pixels to the right
ball.dy = 0.5 # every time the ball is moving, x will be increased 2 pixels to up
# functions
def madrab1_up():
    y = madrab1.ycor() # get the current y coordinate of the object
    y+= 20 #Set the new y coordinate value
    madrab1.sety(y) # set the new location of the object on y axis
def madrab1_down():
    y = madrab1.ycor()
    y-= 20
    madrab1.sety(y)
def madrab2_up():
    y = madrab2.ycor() # get the current location of the object
    y+= 20
    madrab2.sety(y) # set the new location of the object on y axis
def madrab2_down():
    y = madrab2.ycor()
    y-= 20
    madrab2.sety(y)

# Keyboard binding
wind.listen() # tell the window to expect keyboard input
wind.onkeypress(madrab1_up,'w') # when presseng W on keyboard, function madrab1_up is called
wind.onkeypress(madrab1_down,'s')
wind.onkeypress(madrab2_up,'Up')
wind.onkeypress(madrab2_down,'Down')




# main game loop
while True:
    wind.update() # update the screem everytime the loop run

    #move the ball
    ball.setx(ball.xcor() + ball.dx) # ball starts at zero and everytime loops run---+0.5 on x axis
    ball.sety(ball.ycor()+ball.dy) # ball starts at zero and everytime loops run---+0.5 on y axis

    #upper border check, top boarder +300px, bottom boarder -300px, ball is 20 px
    if ball.ycor()>290: # if the ball is at top border
        ball.sety(290) #set y coordinate +290
        ball.dy*=-1 # reverse direction
    #lower border check
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-0.5

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -0.5

     # collision between madrab and ball
    if(ball.xcor()>340 and ball.xcor() <350) and (ball.ycor() <madrab2.ycor()+ 40 and ball.ycor()> madrab2.ycor()-40):
        ball.setx(340)
        ball.dx*=-0.5

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *=-0.5


















