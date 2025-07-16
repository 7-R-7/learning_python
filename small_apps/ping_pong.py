import turtle

wind = turtle.Screen() # initialize screen
wind.title("Ping Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0) # stops the window from updating automatically

p1 = turtle.Turtle()
p1.speed(0) # initializes turtle object
p1.shape("square") # set the speed of the animation
p1.color("blue") # set the color of the shape
p1.shapesize(stretch_wid=5, stretch_len=1) #stretches the shape 
p1.penup() # stops the object from drawing lines
p1.goto(-350, 0) # set the position

p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("red")
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("BLUE :0 | RED :0", align="center", font=("Courier",24,"normal"))

# functions

def p1_up():
    y = p1.ycor()
    y += 25
    p1.sety(y)
    
def p1_down():
    y = p1.ycor()
    y -= 25
    p1.sety(y)

def p2_up():
    y = p2.ycor() #get the y coordinate of p1
    y += 25
    p2.sety(y) #set the new coordinate of p1
    
def p2_down():
    y = p2.ycor()
    y -= 25
    p2.sety(y)
    
#keyboard bindings

wind.listen() # tell the window to expect keyboard input
wind.onkeypress(p1_up, "w") # when pressing 'w' the p1 goes up
wind.onkeypress(p1_down, "s")
wind.onkeypress(p2_up, "Up")
wind.onkeypress(p2_down, "Down")

#main game loop
while True :
    wind.update() #updates the screen
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # border check top border +300px , bottom border -300px , ball 20px
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"BLUE :{score1} | RED :{score2}", align="center", font=("Courier",24,"normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 +=1
        score.clear()
        score.write(f"BLUE :{score1} | RED :{score2}", align="center", font=("Courier",24,"normal"))
        
    # p1 AND ball
    
    if (ball.xcor() > 340 and ball.xcor() <  350 ) and (ball.ycor() < p2.ycor() + 40 and ball.ycor() > p2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < p1.ycor() + 40 and ball.ycor() > p1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1 