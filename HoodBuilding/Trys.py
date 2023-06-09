import turtle
import random

wn = turtle.Screen()
player = turtle.Turtle()
wn.bgcolor("light green")
wn.setup(700, 700)
player.speed(40000)
wn.title("The Chicken Game")
wn.addshape("chicken.gif"), wn.addshape("blue_car_L.gif"), wn.addshape("bush1.gif")
wn.addshape("red_car.gif"), wn.addshape("chick.gif"), wn.addshape("grey_car_L.gif")
wn.addshape("yellow car.gif"), wn.addshape("red_tender.gif"), wn.addshape("roadPattern.gif")
wn.addshape("grass_frame.gif"), wn.addshape("fountain.gif"), wn.addshape("green_tender.gif")
wn.addshape("manCick01.gif"), wn.addshape("manCick02.gif"), wn.addshape("manCick03.gif")
wn.addshape("manCick21.gif"), wn.addshape("manCick22.gif"), wn.addshape("manCick23.gif")
wn.addshape("ball.gif"), wn.addshape("cat1.gif"), wn.addshape("cat2.gif"), wn.addshape("cat1Mirror.gif")
wn.addshape("cat2Mirror.gif")

turtle.tracer(0)

player.hideturtle()


def move():
    if chickenp.direction == "up":
        yPose = chickenp.ycor()
        chickenp.sety(yPose + 6)
        if score >= 200:
            chickenp.sety(yPose + 10)
        if score >= 400:
            chickenp.sety(yPose + 20)
    if chickenp.direction == "down":
        yPose = chickenp.ycor()
        chickenp.sety(yPose - 6)
        if score >= 200:
            chickenp.sety(yPose - 10)
        if score >= 400:
            chickenp.sety(yPose - 20)
    if chickenp.direction == "left":
        xPose = chickenp.xcor()
        chickenp.setx(xPose - 6)
        if score >= 200:
            chickenp.setx(xPose - 10)
        if score >= 400:
            chickenp.setx(xPose - 20)
    if chickenp.direction == "right":
        xPose = chickenp.xcor()
        chickenp.setx(xPose + 6)
        if score >= 200:
            chickenp.setx(xPose + 10)
        if score >= 400:
            chickenp.setx(xPose + 20)

    car_speed = 10
    blueCar.forward(car_speed - 1)
    greyCarMid.forward(car_speed + 4)
    redCar.forward(car_speed)
    redTender.forward(car_speed + 4)
    yellowCar.forward(car_speed)
    greenTender.forward(car_speed + 3)
    ball.forward(4)
    cat.forward(8)

    if redCar.xcor() > 700 and greenTender.xcor() > 700:
        redCar.hideturtle()
        redCar.speed(100000)
        redCar.goto(-730, -213)
        redCar.speed(4)
        redCar.showturtle()

        greenTender.hideturtle()
        greenTender.speed(100000)
        greenTender.goto(-730, 222)
        greenTender.speed(4)
        greenTender.showturtle()

    if blueCar.xcor() < -700:
        blueCar.hideturtle()
        blueCar.speed(100000)
        blueCar.goto(730, -155)
        blueCar.speed(5)
        blueCar.showturtle()

    if greyCarMid.xcor() < -700:
        greyCarMid.hideturtle()
        greyCarMid.speed(100000)
        greyCarMid.goto(730, 69)
        greyCarMid.speed(7)
        greyCarMid.showturtle()

    if redTender.xcor() < -700:
        redTender.hideturtle()
        redTender.speed(100000)
        redTender.goto(850, 64)
        redTender.speed(7)
        redTender.showturtle()

    if yellowCar.xcor() > 700:
        yellowCar.hideturtle()
        yellowCar.speed(100000)
        yellowCar.goto(-730, -217)
        yellowCar.speed(4)
        yellowCar.showturtle()

    if ball.xcor() >= -300:
        ball.speed(0)
        ball.left(180)
        ball.speed(3)
        boy1.shape("manCick02.gif")
        wn.update()
        boy1.shape("manCick03.gif")
        wn.update()
        boy1.shape("manCick01.gif")

    if ball.xcor() <= -420:
        ball.speed(0)
        ball.left(180)
        ball.speed(3)
        boy2.shape("manCick22.gif")
        wn.update()
        boy2.shape("manCick23.gif")
        wn.update()
        boy2.shape("manCick21.gif")

    if cat.xcor() >= -180:
        cat.speed(0)
        cat.left(180)
        wn.update()
        cat.shape("cat1Mirror.gif")
        cat.speed(8)
        wn.update()

    if cat.xcor() <= -480:
        cat.speed(0)
        cat.left(180)
        wn.update()
        cat.shape("cat1.gif")
        cat.speed(8)
        wn.update()

    if score >= 100:
        blueCar.forward(car_speed + 10)
        greyCarMid.forward(car_speed + 14)
        redCar.forward(car_speed + 10)
        redTender.forward(car_speed + 14)
        yellowCar.forward(car_speed + 10)
        greenTender.forward(car_speed + 13)
        ball.forward(4)
    if score >= 200:
        blueCar.forward(car_speed + 20)
        greyCarMid.forward(car_speed + 24)
        redCar.forward(car_speed + 20)
        redTender.forward(car_speed + 24)
        yellowCar.forward(car_speed + 20)
        greenTender.forward(car_speed + 23)
        ball.forward(5)

    if score >= 300:
        blueCar.forward(car_speed + 30)
        greyCarMid.forward(car_speed + 34)
        redCar.forward(car_speed + 30)
        redTender.forward(car_speed + 34)
        yellowCar.forward(car_speed + 30)
        greenTender.forward(car_speed + 33)
        ball.forward(6)

    if score >= 400:
        blueCar.forward(car_speed + 40)
        greyCarMid.forward(car_speed + 44)
        redCar.forward(car_speed + 40)
        redTender.forward(car_speed + 44)
        yellowCar.forward(car_speed + 40)
        greenTender.forward(car_speed + 43)
        ball.forward(7)


def goUp():
    chickenp.direction = "up"


def goDown():
    chickenp.direction = "down"


def goLeft():
    chickenp.direction = "left"


def goRight():
    chickenp.direction = "right"


def draw_highWay_LtoR(x, y, s):
    player.width(2)
    player.setx(x - 50)
    player.sety(y)
    player.pendown()
    player.forward(500)
    player.penup()
    player.setx(x - 50)
    player.sety(y - 130)
    player.pendown()
    player.forward(500)
    player.penup()
    player.setx(x - 40)
    player.sety(y - 65)

    for i in range(s):
        player.fillcolor("white")
        player.pendown()
        player.begin_fill()
        player.forward(25)
        player.right(90)
        player.forward(5)
        player.right(90)
        player.forward(25)
        player.right(90)
        player.forward(5)
        player.right(90)
        player.end_fill()
        player.penup()
        player.forward(50)
        player.pendown()
        player.penup()


def bush(x, y):
    bush1 = turtle.Turtle()
    bush1.penup()
    bush1.hideturtle()
    bush1.shape("bush1.gif")
    bush1.goto(x, y)
    bush1.showturtle()


# grass paint - background :
wn.bgpic("grass_frame.gif")

grassLeft = turtle.Turtle()
grassLeft.hideturtle()
grassLeft.shape("grass_frame.gif")
grassLeft.penup()
grassLeft.goto(-700, 0)
grassLeft.showturtle()

grassRight = turtle.Turtle()
grassRight.hideturtle()
grassRight.shape("grass_frame.gif")
grassRight.penup()
grassRight.goto(700, 0)
grassRight.showturtle()

# create game space :
# road pattern :
# bottom road :
broad = turtle.Turtle()
broad.speed(0)
broad.hideturtle()
broad.shape("roadPattern.gif")
broad.penup()
broad.goto(0, -121.5)
broad.showturtle()
# road bottom right :
broadR = turtle.Turtle()
broadR.speed(0)
broadR.hideturtle()
broadR.shape("roadPattern.gif")
broadR.penup()
broadR.goto(300, -121.5)
broadR.showturtle()
# road bottom left :
broadL = turtle.Turtle()
broadL.speed(0)
broadL.hideturtle()
broadL.shape("roadPattern.gif")
broadL.penup()
broadL.goto(-300, -121.5)
broadL.showturtle()

# middle road :
mroad = turtle.Turtle()
mroad.speed(0)
mroad.hideturtle()
mroad.shape("roadPattern.gif")
mroad.penup()
mroad.goto(0, 97.5)
mroad.showturtle()
# road middle right :
mroadR = turtle.Turtle()
mroadR.speed(0)
mroadR.hideturtle()
mroadR.shape("roadPattern.gif")
mroadR.penup()
mroadR.goto(300, 97.5)
mroadR.showturtle()
# road middle left :
mroadL = turtle.Turtle()
mroadL.speed(0)
mroadL.hideturtle()
mroadL.shape("roadPattern.gif")
mroadL.penup()
mroadL.goto(-300, 97.5)
mroadL.showturtle()

# top road :
troad = turtle.Turtle()
troad.speed(0)
troad.hideturtle()
troad.shape("roadPattern.gif")
troad.penup()
troad.goto(0, 317.5)
troad.showturtle()
# road top right :
troadR = turtle.Turtle()
troadR.speed(0)
troadR.hideturtle()
troadR.shape("roadPattern.gif")
troadR.penup()
troadR.goto(300, 317.5)
troadR.showturtle()
# road top left :
troadL = turtle.Turtle()
troadL.speed(0)
troadL.hideturtle()
troadL.shape("roadPattern.gif")
troadL.penup()
troadL.goto(-300, 317.5)
troadL.showturtle()

player.penup()
draw_highWay_LtoR(500, -120, 10)
draw_highWay_LtoR(0, -120, 10)
draw_highWay_LtoR(-500, -120, 10)
draw_highWay_LtoR(-1000, -120, 10)
draw_highWay_LtoR(-1000, 100, 10)
draw_highWay_LtoR(-500, 100, 10)
draw_highWay_LtoR(0, 100, 10)
draw_highWay_LtoR(500, 100, 10)
draw_highWay_LtoR(0, 320, 10)
draw_highWay_LtoR(500, 320, 10)
draw_highWay_LtoR(-500, 320, 10)
draw_highWay_LtoR(-1000, 320, 10)

# create decorate shapes :
# cat :
cat = turtle.Turtle()
cat.hideturtle()
cat.shape("cat1.gif")
cat.penup()
cat.goto(-280, -80)
cat.showturtle()
# water fountain :
fountain = turtle.Turtle()
fountain.hideturtle()
fountain.shape("fountain.gif")
fountain.penup()
fountain.goto(320, -80)
fountain.showturtle()

# boys play with ball :
boy1 = turtle.Turtle()
boy1.hideturtle()
boy1.shape("manCick01.gif")
boy1.penup()
boy1.goto(-300, 150)
boy1.showturtle()

boy2 = turtle.Turtle()
boy2.hideturtle()
boy2.shape("manCick21.gif")
boy2.penup()
boy2.goto(-450, 150)
boy2.showturtle()

ball = turtle.Turtle()
ball.hideturtle()
ball.shape("ball.gif")
ball.penup()
ball.goto(-420, 130)
ball.showturtle()
ball.diraction = "right"

# create players :

# red car :
redCar = turtle.Turtle()
redCar.speed(1)
redCar.hideturtle()
redCar.shape("red_car.gif")
redCar.penup()
redCar.goto(-730, -213)
redCar.showturtle()
redCar.diraction = "right"

# green tender :
greenTender = turtle.Turtle()
greenTender.speed(1)
greenTender.hideturtle()
greenTender.shape("green_tender.gif")
greenTender.penup()
greenTender.goto(-730, 222)
greenTender.showturtle()
greenTender.diraction = "right"

# yellow car :
yellowCar = turtle.Turtle()
yellowCar.speed(1)
yellowCar.hideturtle()
yellowCar.shape("yellow car.gif")
yellowCar.penup()
yellowCar.goto(-1000, -217)
yellowCar.showturtle()
yellowCar.diraction = "right"

# blue car bottom road:
blueCar = turtle.Turtle()
blueCar.speed(1)
blueCar.hideturtle()
blueCar.shape("blue_car_L.gif")
blueCar.penup()
blueCar.goto(730, -153)
blueCar.showturtle()
blueCar.left(180)

# grey car mid road :
greyCarMid = turtle.Turtle()
greyCarMid.speed(1)
greyCarMid.hideturtle()
greyCarMid.shape("grey_car_L.gif")
greyCarMid.penup()
greyCarMid.goto(730, 69)
greyCarMid.showturtle()
greyCarMid.left(180)

# red tender mid road :
redTender = turtle.Turtle()
redTender.speed(1)
redTender.hideturtle()
redTender.shape("red_tender.gif")
redTender.penup()
redTender.goto(900, 64)
redTender.showturtle()
redTender.left(180)

# chicken:
chickenp = turtle.Turtle()
chickenp.penup()
chickenp.hideturtle()
chickenp.shape("chicken.gif")
chickenp.goto(0, -290)
chickenp.showturtle()
chickenp.speed(0)
chickenp.direction = "stop"

# chick :
chick = turtle.Turtle()
chick.speed(0)
chick.shape("chick.gif")
chick.color("red")
chick.penup()
chick.goto(100, 100)
turtle.tracer(1)
wn.listen()
wn.onkeypress(goUp, "Up")
wn.onkeypress(goDown, "Down")
wn.onkeypress(goLeft, "Left")
wn.onkeypress(goRight, "Right")

# score :
score = 0
score_string = "score : %s" % score
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(-550, 300)
score_pen.color("red")
score_pen.write(score_string, False, font=("Arial", 17, "normal"))
# levels :
levelString = "level up ! "
levels_pen = turtle.Turtle()
levels_pen.penup()
levels_pen.hideturtle()


def play_again():
    global gameOver
    gameOver.hideturtle()
    score = 0
    while True:
        wn.update()

        if chickenp.distance(chick) < 20:
            x = random.randint(-300, 300)
            y = random.randint(-300, 300)
            chick.goto(x, y)
            score += 10
            scoreString = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scoreString, False, font=("Arial", 14, "normal"))

            # show levels on screen :
            if score == 100:
                levelString2 = "your level is : 2"
                levels_pen.goto(-60, 50)
                levels_pen.color("red")
                levels_pen.write(levelString, False, font=("Arial", 20, "normal"))
                levels_pen.goto(-80, 0)
                levels_pen.write(levelString2, False, font=("Arial", 19, "normal"))
                turtle.ontimer(levels_pen.clear, 1500)
                turtle.ontimer(levels_pen.hideturtle, 1500)
            if score == 200:
                levelString2 = "your level is : 3"
                levels_pen.goto(-60, 50)
                levels_pen.color("red")
                levels_pen.write(levelString, False, font=("Arial", 20, "normal"))
                levels_pen.goto(-80, 0)
                levels_pen.write(levelString2, False, font=("Arial", 19, "normal"))
                turtle.ontimer(levels_pen.clear, 1500)
                turtle.ontimer(levels_pen.hideturtle, 1500)
            if score == 300:
                levelString2 = "your level is : 4"
                levels_pen.goto(-60, 50)
                levels_pen.color("red")
                levels_pen.write(levelString, False, font=("Arial", 20, "normal"))
                levels_pen.goto(-80, 0)
                levels_pen.write(levelString2, False, font=("Arial", 19, "normal"))
                turtle.ontimer(levels_pen.clear, 1500)
                turtle.ontimer(levels_pen.hideturtle, 1500)
            if score == 400:
                levelString2 = "your level is : 5"
                levels_pen.goto(-60, 50)
                levels_pen.color("red")
                levels_pen.write(levelString, False, font=("Arial", 20, "normal"))
                levels_pen.goto(-80, 0)
                levels_pen.write(levelString2, False, font=("Arial", 19, "normal"))
                turtle.ontimer(levels_pen.clear, 1500)
                turtle.ontimer(levels_pen.hideturtle, 1500)

        if chickenp.ycor() > 340:
            x = chickenp.xcor()
            chickenp.goto(x, -340)

        if chickenp.ycor() < -340:
            x = chickenp.xcor()
            chickenp.goto(x, 340)

        if chickenp.xcor() < -650:
            y = chickenp.ycor()
            chickenp.goto(650, y)

        if chickenp.xcor() > 650:
            y = chickenp.ycor()
            chickenp.goto(-650, y)

        # crashes :
        if chickenp.distance(redCar) < 45:
            gameOver.hideturtle()
            gameOver.penup()
            gameOver.goto(-200, 0)
            gameOver_string = "Game Over !"
            gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
            gameOver.goto(-190, -100)
            gameOverScore = "your score is : %s" % score
            gameOver.write(gameOverScore, font=("Arial", 50, "normal"))
            wn.exitonclick()

        if chickenp.distance(greyCarMid) < 45:
            gameOver.hideturtle()
            gameOver.penup()
            gameOver.goto(-200, 0)
            gameOver_string = "Game Over !"
            gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
            gameOver.goto(-190, -100)
            gameOverScore = "your score is : %s" % score
            gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
            wn.exitonclick()

        if chickenp.distance(blueCar) < 45:
            gameOver.hideturtle()
            gameOver.penup()
            gameOver.goto(-200, 0)
            gameOver_string = "Game Over !"
            gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
            gameOver.goto(-190, -100)
            gameOverScore = "your score is : %s" % score
            gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
            wn.exitonclick()

        if chickenp.distance(redTender) < 45:
            gameOver = turtle.Turtle()
            gameOver.hideturtle()
            gameOver.penup()
            gameOver.goto(-200, 0)
            gameOver_string = "Game Over !"
            gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
            gameOver.goto(-190, -100)
            gameOverScore = "your score is : %s" % score
            gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
            wn.exitonclick()

        if chickenp.distance(greenTender) < 45:
            gameOver.hideturtle()
            gameOver.penup()
            gameOver.goto(-200, 0)
            gameOver_string = "Game Over !"
            gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
            gameOver.goto(-190, -100)
            gameOverScore = "your score is : %s" % score
            gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
            wn.exitonclick()

        if chickenp.distance(fountain) < 40:
            gameOver = turtle.Turtle()
            gameOver.hideturtle()
            gameOver.penup()
            gameOver.goto(-350, 0)
            gameOverDrawn = "THE CHICKEN DOESN'T KNOW TO SWIM !"
            gameOver.write(gameOverDrawn, font=("Arial", 30, "normal"))
            gameOver.goto(-200, -80)
            gameOver_string = "Game Over !"
            gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
            gameOver.goto(-160, -120)
            gameOverScore = "your score is : %s" % score
            gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
            wn.exitonclick()

        if chickenp.distance(ball) < 20:
            gameOver = turtle.Turtle()
            gameOver.hideturtle()
            gameOver.penup()
            gameOver.goto(-350, 0)
            gameOverDrawn = "YOU GOT HITTED BY THE BALL !"
            gameOver.write(gameOverDrawn, font=("Arial", 30, "normal"))
            gameOver.goto(-200, -80)
            gameOver_string = "Game Over !"
            gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
            gameOver.goto(-160, -120)
            gameOverScore = "your score is : %s" % score
            gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
            wn.exitonclick()

        if chickenp.distance(cat) < 20:
            gameOver = turtle.Turtle()
            gameOver.hideturtle()
            gameOver.penup()
            gameOver.goto(-350, 0)
            gameOverDrawn = "YOU GOT EATEN BY THE CAT !"
            gameOver.write(gameOverDrawn, font=("Arial", 30, "normal"))
            gameOver.goto(-200, -80)
            gameOver_string = "Game Over !"
            gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
            gameOver.goto(-160, -120)
            gameOverScore = "your score is : %s" % score
            gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
            wn.exitonclick()

        move()

    pass


while True:
    wn.update()

    if chickenp.distance(chick) < 20:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        chick.goto(x, y)
        score += 10
        scoreString = "Score: %s" % score
        score_pen.clear()
        score_pen.write(scoreString, False, font=("Arial", 14, "normal"))

        # show levels on screen :
        if score == 100:
            levelString2 = "your level is : 2"
            levels_pen.goto(-60, 50)
            levels_pen.color("red")
            levels_pen.write(levelString, False, font=("Arial", 20, "normal"))
            levels_pen.goto(-80, 0)
            levels_pen.write(levelString2, False, font=("Arial", 19, "normal"))
            turtle.ontimer(levels_pen.clear, 1500)
            turtle.ontimer(levels_pen.hideturtle, 1500)
        if score == 200:
            levelString2 = "your level is : 3"
            levels_pen.goto(-60, 50)
            levels_pen.color("red")
            levels_pen.write(levelString, False, font=("Arial", 20, "normal"))
            levels_pen.goto(-80, 0)
            levels_pen.write(levelString2, False, font=("Arial", 19, "normal"))
            turtle.ontimer(levels_pen.clear, 1500)
            turtle.ontimer(levels_pen.hideturtle, 1500)
        if score == 300:
            levelString2 = "your level is : 4"
            levels_pen.goto(-60, 50)
            levels_pen.color("red")
            levels_pen.write(levelString, False, font=("Arial", 20, "normal"))
            levels_pen.goto(-80, 0)
            levels_pen.write(levelString2, False, font=("Arial", 19, "normal"))
            turtle.ontimer(levels_pen.clear, 1500)
            turtle.ontimer(levels_pen.hideturtle, 1500)
        if score == 400:
            levelString2 = "your level is : 5"
            levels_pen.goto(-60, 50)
            levels_pen.color("red")
            levels_pen.write(levelString, False, font=("Arial", 20, "normal"))
            levels_pen.goto(-80, 0)
            levels_pen.write(levelString2, False, font=("Arial", 19, "normal"))
            turtle.ontimer(levels_pen.clear, 1500)
            turtle.ontimer(levels_pen.hideturtle, 1500)

    if chickenp.ycor() > 340:
        x = chickenp.xcor()
        chickenp.goto(x, -340)

    if chickenp.ycor() < -340:
        x = chickenp.xcor()
        chickenp.goto(x, 340)

    if chickenp.xcor() < -650:
        y = chickenp.ycor()
        chickenp.goto(650, y)

    if chickenp.xcor() > 650:
        y = chickenp.ycor()
        chickenp.goto(-650, y)

    # crashes :
    if chickenp.distance(redCar) < 45:
        gameOver = turtle.Turtle()
        gameOver.hideturtle()
        gameOver.penup()
        gameOver.goto(-200, 0)
        gameOver_string = "Game Over !"
        gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
        gameOver.goto(-190, -100)
        gameOverScore = "your score is : %s" % score
        gameOver.write(gameOverScore, font=("Arial", 50, "normal"))
        play_button = turtle.Turtle()
        play_button.penup()
        play_button.shape("square")
        play_button.color("white")
        play_button.goto(0, -200)
        play_button.write("Play Again", align="center", font=("Arial", 16, "bold"))
        play_button.onclick(play_again)

    if chickenp.distance(greyCarMid) < 45:
        gameOver = turtle.Turtle()
        gameOver.hideturtle()
        gameOver.penup()
        gameOver.goto(-200, 0)
        gameOver_string = "Game Over !"
        gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
        gameOver.goto(-190, -100)
        gameOverScore = "your score is : %s" % score
        gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
        play_button = turtle.Turtle()
        play_button.penup()
        play_button.shape("square")
        play_button.color("white")
        play_button.goto(0, -200)
        play_button.write("Play Again", align="center", font=("Arial", 16, "bold"))
        play_button.onclick(play_again)

    if chickenp.distance(blueCar) < 45:
        gameOver = turtle.Turtle()
        gameOver.hideturtle()
        gameOver.penup()
        gameOver.goto(-200, 0)
        gameOver_string = "Game Over !"
        gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
        gameOver.goto(-190, -100)
        gameOverScore = "your score is : %s" % score
        gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
        play_button = turtle.Turtle()
        play_button.penup()
        play_button.shape("square")
        play_button.color("white")
        play_button.goto(0, -200)
        play_button.write("Play Again", align="center", font=("Arial", 16, "bold"))
        play_button.onclick(play_again)

    if chickenp.distance(redTender) < 45:
        gameOver = turtle.Turtle()
        gameOver.hideturtle()
        gameOver.penup()
        gameOver.goto(-200, 0)
        gameOver_string = "Game Over !"
        gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
        gameOver.goto(-190, -100)
        gameOverScore = "your score is : %s" % score
        gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
        play_button = turtle.Turtle()
        play_button.penup()
        play_button.shape("square")
        play_button.color("white")
        play_button.goto(0, -200)
        play_button.write("Play Again", align="center", font=("Arial", 16, "bold"))
        play_button.onclick(play_again)

    if chickenp.distance(greenTender) < 45:
        gameOver = turtle.Turtle()
        gameOver.hideturtle()
        gameOver.penup()
        gameOver.goto(-200, 0)
        gameOver_string = "Game Over !"
        gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
        gameOver.goto(-190, -100)
        gameOverScore = "your score is : %s" % score
        gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
        play_button = turtle.Turtle()
        play_button.penup()
        play_button.shape("square")
        play_button.color("white")
        play_button.goto(0, -200)
        play_button.write("Play Again", align="center", font=("Arial", 16, "bold"))
        play_button.onclick(play_again)

    if chickenp.distance(fountain) < 40:
        gameOver = turtle.Turtle()
        gameOver.hideturtle()
        gameOver.penup()
        gameOver.goto(-350, 0)
        gameOverDrawn = "THE CHICKEN DOESN'T KNOW TO SWIM !"
        gameOver.write(gameOverDrawn, font=("Arial", 30, "normal"))
        gameOver.goto(-200, -80)
        gameOver_string = "Game Over !"
        gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
        gameOver.goto(-160, -120)
        gameOverScore = "your score is : %s" % score
        gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
        play_button = turtle.Turtle()
        play_button.penup()
        play_button.shape("square")
        play_button.color("white")
        play_button.goto(0, -200)
        play_button.write("Play Again", align="center", font=("Arial", 16, "bold"))
        play_button.onclick(play_again)

    if chickenp.distance(ball) < 20:
        gameOver = turtle.Turtle()
        gameOver.hideturtle()
        gameOver.penup()
        gameOver.goto(-350, 0)
        gameOverDrawn = "YOU GOT HITTED BY THE BALL !"
        gameOver.write(gameOverDrawn, font=("Arial", 30, "normal"))
        gameOver.goto(-200, -80)
        gameOver_string = "Game Over !"
        gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
        gameOver.goto(-160, -120)
        gameOverScore = "your score is : %s" % score
        gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
        play_button = turtle.Turtle()
        play_button.penup()
        play_button.shape("square")
        play_button.color("white")
        play_button.goto(0, -200)
        play_button.write("Play Again", align="center", font=("Arial", 16, "bold"))
        play_button.onclick(play_again)

    if chickenp.distance(cat) < 20:
        gameOver = turtle.Turtle()
        gameOver.hideturtle()
        gameOver.penup()
        gameOver.goto(-350, 0)
        gameOverDrawn = "YOU GOT EATEN BY THE CAT !"
        gameOver.write(gameOverDrawn, font=("Arial", 30, "normal"))
        gameOver.goto(-200, -80)
        gameOver_string = "Game Over !"
        gameOver.write(gameOver_string, font=("Arial", 50, "normal"))
        gameOver.goto(-160, -120)
        gameOverScore = "your score is : %s" % score
        gameOver.write(gameOverScore, font=("Arial", 30, "normal"))
        play_button = turtle.Turtle()
        play_button.penup()
        play_button.shape("square")
        play_button.color("white")
        play_button.goto(0, -200)
        play_button.write("Play Again", align="center", font=("Arial", 16, "bold"))
        play_button.onclick(play_again)

    move()

wn.mainloop()
