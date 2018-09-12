import turtle, time, sys, random
turtle.tracer(0, 0)
turtle.setup( width = 710, height = 700, startx = None, starty = None)
tu = turtle.Turtle()
tu.shape("square")
tu.color("yellow")
time.sleep(10)
tu.up()
tu.turtlesize(2)
tu.sety(50)
tu.speed(0)
tu.setx(-200)
def flap():
    global velocity
    velocity = 10
def flap1(x, y):
    if (x, y) == tu.pos():
        gameover()
    global velocity
    velocity = 10      
turtleOffset = 21
setup = turtle.Turtle()
setup.up()
setup.ht()
pipe1 = turtle.Turtle()
pipe1.ht()
pipe1.up()
pipe1.color("green")
def drawPipe(pipe, x, y):
    pipe.setpos(x, y)
    pipe.begin_fill()
    pipe.seth(0)
    for i in range(2):
        pipe.forward(100)
        pipe.right(90)
        pipe.forward(450)
        pipe.right(90)
    pipe.end_fill()
    pipe.sety(pipe.ycor()-550)
    pipe.begin_fill()
    for i in range(2):
        pipe.forward(100)
        pipe.right(90)
        pipe.forward(450)
        pipe.right(90)
    pipe.end_fill()
score = 0
scoreCounted = False
setup.speed(0)
setup.setpos(-360, -180)
def setupRect():
    setup.seth(0)
    setup.begin_fill()
    setup.forward(730)
    setup.right(90)
    setup.forward(200)
    setup.right(90)
    setup.forward(730)
    setup.right(90)
    setup.forward(200)
    setup.end_fill()
setupRect()
setup.setpos(-360, 395)
setupRect()
velocity = 0.0
terminalVelocity = [30, -30]
window = turtle.Screen()
window.onclick(flap1)
window.listen()
pipePos = [360, 500]
drawPipe(pipe1, 0, 0)
def gameover():
    window.onclick(None)
    velocity = 0
    time.sleep(0.4)
    for i in range(400):
        turtle.update()
        if not velocity in terminalVelocity:
            velocity += -0.8
            tu.sety(tu.ycor()+velocity)
            tu.setx(tu.xcor()+3)
    sys.exit()   
def checkScore():
    global score, scoreCounted
    if tu.xcor() > pipePos[0]+100:
        if scoreCounted == False:
            score += 1
            scoreify(score)
            scoreCounted = True
drawturt = turtle.Turtle()
drawturt.up()
drawturt.ht()
drawturt.color("white")
def scoreify(x):
    global drawturt
    drawturt.clear()
    drawturt.setpos(290, 200)
    drawturt.write(x, font=("Arial", 40, "normal"), align = "center")
def check():
    if tu.ycor() < -173 or tu.ycor() > 180:
        gameover()
def checkPipe():
    if tu.ycor() > pipePos[1]-465 or tu.ycor() < pipePos[1]-535:
        if tu.xcor() > pipePos[0]-15 and tu.xcor() < pipePos[0]+130:
            gameover()
def newPipe():
    global scoreCounted
    scoreCounted = False
    pipePos[0] = 390
    pipePos[1] = random.randint(400, 650)
scoreify(score)
while True:
    checkScore()
    pipe1.clear()
    drawPipe(pipe1, pipePos[0], pipePos[1])
    pipePos[0] -= 10
    if pipePos[0] < -500:
        newPipe()
    turtle.setup( width = 710, height = 700, startx = None, starty = None)
    time.sleep(0.01)
    if not velocity in terminalVelocity:
        velocity += -0.8
    tu.sety(tu.ycor()+velocity)
    check()
    checkPipe()
    turtle.update()
