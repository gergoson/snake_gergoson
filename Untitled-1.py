
from glob import glob
from random import randint
import turtle

wn = turtle.Screen()
wn.title("thing")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score 0", align="center", font=("Courier", 24, "normal"))

#Score
score = 0

#Player
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("dark green")
player.penup()
player.goto(0,0)
movement_dir = 5
time = 0

#Trails
trail1 = turtle.Turtle()
trail2 = turtle.Turtle()
trail2.speed(0)
trail2.shape("square")
trail2.color("green")
trail2.penup()
trail2.goto(999,999)
trail3 = turtle.Turtle()
trail3.speed(0)
trail3.shape("square")
trail3.color("green")
trail3.penup()
trail3.goto(999,999)
trail4 = turtle.Turtle()
trail4.speed(0)
trail4.shape("square")
trail4.color("green")
trail4.penup()
trail4.goto(999,999)
trail5 = turtle.Turtle()
trail5.speed(0)
trail5.shape("square")
trail5.color("green")
trail5.penup()
trail5.goto(999,999)
trail6 = turtle.Turtle()
trail6.speed(0)
trail6.shape("square")
trail6.color("green")
trail6.penup()
trail6.goto(999,999)
trail7 = turtle.Turtle()
trail7.speed(0)
trail7.shape("square")
trail7.color("green")
trail7.penup()
trail7.goto(999,999)
trail8 = turtle.Turtle()
trail8.speed(0)
trail8.shape("square")
trail8.color("green")
trail8.penup()
trail8.goto(999,999)
trail9 = turtle.Turtle()
trail9.speed(0)
trail9.shape("square")
trail9.color("green")
trail9.penup()
trail9.goto(999,999)
trail10 = turtle.Turtle()
trail10.speed(0)
trail10.shape("square")
trail10.color("green")
trail10.penup()
trail10.goto(999,999)
trail11 = turtle.Turtle()
trail11.speed(0)
trail11.shape("square")
trail11.color("green")
trail11.penup()
trail11.goto(999,999)
trail12 = turtle.Turtle()
trail12.speed(0)
trail12.shape("square")
trail12.color("green")
trail12.penup()
trail12.goto(999,999)
trail13 = turtle.Turtle()
trail13.speed(0)
trail13.shape("square")
trail13.color("green")
trail13.penup()
trail13.goto(999,999)
trail14 = turtle.Turtle()
trail14.speed(0)
trail14.shape("square")
trail14.color("green")
trail14.penup()
trail14.goto(999,999)
trail15 = turtle.Turtle()
trail15.speed(0)
trail15.shape("square")
trail15.color("green")
trail15.penup()
trail15.goto(999,999)
trail16 = turtle.Turtle()
trail16.speed(0)
trail16.shape("square")
trail16.color("green")
trail16.penup()
trail16.goto(999,999)
trail17 = turtle.Turtle()
trail17.speed(0)
trail17.shape("square")
trail17.color("green")
trail17.penup()
trail17.goto(999,999)
trail17 = turtle.Turtle()
trail17.speed(0)
trail17.shape("square")
trail17.color("green")
trail17.penup()
trail17.goto(999,999)
trail18 = turtle.Turtle()
trail18.speed(0)
trail18.shape("square")
trail18.color("green")
trail18.penup()
trail18.goto(999,999)
trail19 = turtle.Turtle()
trail19.speed(0)
trail19.shape("square")
trail19.color("green")
trail19.penup()
trail19.goto(999,999)
trail20 = turtle.Turtle()
trail20.speed(0)
trail20.shape("square")
trail20.color("green")
trail20.penup()
trail20.goto(999,999)
trail21 = turtle.Turtle()
trail21.speed(0)
trail21.shape("square")
trail21.color("green")
trail21.penup()
trail21.goto(999,999)
trail22 = turtle.Turtle()
trail22.speed(0)
trail22.shape("square")
trail22.color("green")
trail22.penup()
trail22.goto(999,999)
trail23 = turtle.Turtle()
trail23.speed(0)
trail23.shape("square")
trail23.color("green")
trail23.penup()
trail23.goto(999,999)
trail24 = turtle.Turtle()
trail24.speed(0)
trail24.shape("square")
trail24.color("green")
trail24.penup()
trail24.goto(999,999)
trail25 = turtle.Turtle()
trail25.speed(0)
trail25.shape("square")
trail25.color("green")
trail25.penup()
trail25.goto(999,999)


#Point
point = turtle.Turtle()
point.shape("circle")
point.color("gold")
point.penup()
point.goto(0,40)

#Fake Point
fpoint1 = turtle.Turtle()
fpoint1.shape("circle")
fpoint1.color("yellow")
fpoint1.penup()
fpoint1.goto(400,400)

fpoint2 = turtle.Turtle()
fpoint2.shape("circle")
fpoint2.color("yellow")
fpoint2.penup()
fpoint2.goto(400,400)

fpoint3 = turtle.Turtle()
fpoint3.shape("circle")
fpoint3.color("yellow")
fpoint3.penup()
fpoint3.goto(400,400)

fpoint4 = turtle.Turtle()
fpoint4 .shape("circle")
fpoint4.color("yellow")
fpoint4.penup()
fpoint4.goto(400,400)

fpoint5 = turtle.Turtle()
fpoint5.shape("circle")
fpoint5.color("yellow")
fpoint5.penup()
fpoint5.goto(400,400)

fpoint6 = turtle.Turtle()
fpoint6.shape("circle")
fpoint6.color("yellow")
fpoint6.penup()
fpoint6.goto(400,400)

fpoint7 = turtle.Turtle()
fpoint7.shape("circle")
fpoint7.color("yellow")
fpoint7.penup()
fpoint7.goto(400,400)

fpoint8 = turtle.Turtle()
fpoint8.shape("circle")
fpoint8.color("yellow")
fpoint8.penup()
fpoint8.goto(400,400)

fpoint9 = turtle.Turtle()
fpoint9.shape("circle")
fpoint9.color("yellow")
fpoint9.penup()
fpoint9.goto(400,400)

#Gates
gate_en = turtle.Turtle()
gate_en.shape("circle")
gate_en.color("dark blue")
gate_en.penup()
gate_en.goto(400,400)

gate_ex = turtle.Turtle()
gate_ex.shape("circle")
gate_ex.color("dark blue")
gate_ex.penup()
gate_ex.goto(400,400)

#Mines
mine1 = turtle.Turtle()
mine1.shape("circle")
mine1.color("dark blue")
mine1.penup()
mine1.goto(400,400)

mine2 = turtle.Turtle()
mine2.shape("circle")
mine2.color("dark blue")
mine2.penup()
mine2.goto(400,400)

mine3 = turtle.Turtle()
mine3.shape("circle")
mine3.color("dark blue")
mine3.penup()
mine3.goto(400,400)

#Function
def spawn():
  trail1.speed(0)
  trail1.shape("square")
  trail1.color("green")
  trail1.penup()
  if score > 22:
   trail25.goto(trail24.xcor(),trail24.ycor())
  if score > 21:
   trail24.goto(trail23.xcor(),trail23.ycor())
  if score > 20:
   trail23.goto(trail22.xcor(),trail22.ycor())
  if score > 20:
   trail22.goto(trail21.xcor(),trail21.ycor())
  if score > 19:
   trail21.goto(trail20.xcor(),trail20.ycor())
  if score > 18:
   trail20.goto(trail19.xcor(),trail19.ycor())
  if score > 17:
   trail19.goto(trail18.xcor(),trail18.ycor())
  if score > 16:
   trail18.goto(trail17.xcor(),trail17.ycor())
  if score > 15:
   trail17.goto(trail16.xcor(),trail16.ycor())
  if score > 14:
   trail16.goto(trail15.xcor(),trail15.ycor())
  if score > 13:
   trail15.goto(trail14.xcor(),trail14.ycor())
  if score > 12:
   trail14.goto(trail13.xcor(),trail13.ycor())
  if score > 11:
   trail13.goto(trail12.xcor(),trail12.ycor())
  if score > 10:
   trail12.goto(trail11.xcor(),trail11.ycor())
  if score > 9:
   trail11.goto(trail10.xcor(),trail10.ycor())
  if score > 8:
   trail10.goto(trail9.xcor(),trail9.ycor())
  if score > 7:
   trail9.goto(trail8.xcor(),trail8.ycor())
  if score > 6:
   trail8.goto(trail7.xcor(),trail7.ycor())
  if score > 5:
   trail7.goto(trail6.xcor(),trail6.ycor())
  if score > 4:
   trail6.goto(trail5.xcor(),trail5.ycor())
  if score > 3:
   trail5.goto(trail4.xcor(),trail4.ycor())
  if score > 2:
   trail4.goto(trail3.xcor(),trail3.ycor())
  if score > 1:
   trail3.goto(trail2.xcor(),trail2.ycor())
  if score > 0:
    trail2.goto(trail1.xcor(),trail1.ycor())
  trail1.goto(player.xcor(),player.ycor())

def player_up():
   global movement_dir
   if movement_dir != 2:
    movement_dir = 1
    
def player_down():
   global movement_dir
   if movement_dir != 1:
    movement_dir = 2

def player_right():
   global movement_dir
   if movement_dir != 4:
    movement_dir = 3

def player_left():
   global movement_dir
   if movement_dir != 3:
    movement_dir = 4

def fpoint1_respawn():
  pr1 = randint(-3,3)
  pr2 = randint(-3,3)
  fpoint1.goto(pr1 * 80,pr2 * 80)
    
def fpoint2_respawn():
  pr1 = randint(-3,3)
  pr2 = randint(-3,3)
  fpoint2.goto(pr1 * 80,pr2 * 80)



def fpoint3_respawn():
  pr1 = randint(-3,3)
  pr2 = randint(-3,3)
  fpoint3.goto(pr1 * 80,pr2 * 80)

def fpoint4_respawn():
  pr1 = randint(-3,3)
  pr2 = randint(-3,3)
  fpoint4.goto(pr1 * 80,pr2 * 80)

def fpoint5_respawn():
  pr1 = randint(-3,3)
  pr2 = randint(-3,3)
  fpoint5.goto(pr1 * 80,pr2 * 80)

def gate_ex_respawn():
  gr1 = randint(-4,4)
  gr2 = randint(-4,4)
  gate_ex.goto(gr1 * 60,gr2 * 60)

def gate_en_respawn():
  gr1 = randint(-4,4)
  gr2 = randint(-4,4)
  gate_en.goto(gr1 * 60,gr2 * 60)

def fpoint6_respawn():
  pr1 = randint(-3,3)
  pr2 = randint(-3,3)
  fpoint6.goto(pr1 * 80,pr2 * 80)

def fpoint7_respawn():
  pr1 = randint(-3,3)
  pr2 = randint(-3,3)
  fpoint7.goto(pr1 * 80,pr2 * 80)

def fpoint8_respawn():
  pr1 = randint(-3,3)
  pr2 = randint(-3,3)
  fpoint8.goto(pr1 * 80,pr2 * 80)

def fpoint9_respawn():
  pr1 = randint(-3,3)
  pr2 = randint(-3,3)
  fpoint9.goto(pr1 * 80,pr2 * 80)

def game_over():
    global movement_dir
    movement_dir = "ass"
    player.goto(0,0)
    wn.clearscreen()
    wn.bgcolor("dark red")
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("red")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("Game Over", align="center", font=("Courier", 80, "normal"))
    dmv = randint(1,11)
    if dmv == 1:
      dmessage = "You fucking suck."
    if dmv == 2:
      dmessage = "Did you seriously just lose at snake?"
    if dmv == 3:
      dmessage = "Just give up already!"
    if dmv == 4:
      dmessage = "I'm almost embarassed for you."
    if dmv == 5:
      dmessage = "What are you doing with your life?"
    if dmv == 6:
      dmessage = "How can someone possibly be this bad at snake?"
    if dmv == 7:
      dmessage = "Why are you still trying?"
    if dmv == 8:
      dmessage = "Great fucking job, dumbass!"
    if dmv == 9:
      dmessage = "Get fucked!"
    if dmv == 10:
      dmessage = "Having fun, bitch?"
    if dmv == 11:
      dmessage = "..."
    pen2 = turtle.Turtle()
    pen2.speed(0)
    pen2.shape("square")
    pen2.color("red")
    pen2.penup()
    pen2.hideturtle()
    pen2.goto(0,-20)
    pen2.write("{}".format(dmessage), align="center", font=("Courier", 14, "normal"))
    pen3 = turtle.Turtle()
    pen3.speed(0)
    pen3.shape("square")
    pen3.color("red")
    pen3.penup()
    pen3.hideturtle()
    pen3.goto(0,-280)
    pen3.write("Press E to restart.", align="center", font=("Courier", 20, "normal"))

def point_respawn():
    pr1 = randint(-7,7)
    pr2 = randint(-7,7)
    point.goto(pr1 * 40,pr2 * 40)
    if score == 25:
      player.goto(0,0)
      wn.clearscreen()
      wn.bgcolor("gold")
      pen = turtle.Turtle()
      pen.speed(0)
      pen.shape("square")
      pen.color("yellow")
      pen.penup()
      pen.hideturtle()
      pen.goto(0, 0)
      pen.write("You Win!", align="center", font=("Courier", 80, "normal"))
    #if score > 2:
     #fpoint1_respawn()
    #if score > 5:
     #fpoint2_respawn()
    #if score > 6:
      #mine1_respawn()
    #if score > 8:
      #fpoint3_respawn()
    #if score > 11:
      #fpoint4_respawn()
    #if score > 13:
      #mine2_respawn()
    #if score > 14:
      #fpoint5_respawn()
    #if score > 15:
      #gate_en_respawn()
    #if score > 15:
      #gate_ex_respawn()
    #if score > 17:
      #fpoint6_respawn()
    #if score > 20:
      #fpoint7_respawn()
    #if score > 20:
      #mine3_respawn()
    #if score > 23:
      #fpoint9_respawn()
    
#Keyboard binding
wn.listen()
wn.onkeypress(player_up, "w")
wn.onkeypress(player_down, "s")
wn.onkeypress(player_left, "a")
wn.onkeypress(player_right, "d")
wn.onkeypress(point_respawn, "p")
wn.onkeypress(game_over, "g")
wn.onkeypress(fpoint1_respawn,"h")


#Main game loop


while True:
    wn.update()
    time += 1

    if movement_dir == 1 and time > 89:
       spawn()
       y = player.ycor() + 20
       player.sety(y) 
       time = 0

    if movement_dir == 2 and time > 89:
       spawn()
       y = player.ycor() - 20
       player.sety(y) 
       time = 0

    if movement_dir == 3 and time > 89:
       spawn()
       x = player.xcor() + 20
       player.setx(x) 
       time = 0

    if movement_dir == 4 and time > 89:
       spawn()
       x = player.xcor() - 20
       player.setx(x) 
       time = 0
    
    #Player-Wall collision
    if player.ycor() > 290:
      game_over()
    if player.ycor() < -290:
      game_over()
    if player.xcor() > 290:
      game_over()
    if player.xcor() < -290:
      game_over()

    #Point pickup
    if player.ycor() == point.ycor() and player.xcor() == point.xcor():
     
     score += 1
     pen.clear()
     pen.write("Score {}".format(score), align="center", font=("Courier", 24, "normal"))
     point_respawn()

    #Player-trail collision
    if player.ycor() == trail4.ycor() and player.xcor() == trail4.xcor():
      game_over()
    if player.ycor() == trail5.ycor() and player.xcor() == trail5.xcor():
      game_over()
    if player.ycor() == trail6.ycor() and player.xcor() == trail6.xcor():
      game_over()
    if player.ycor() == trail7.ycor() and player.xcor() == trail7.xcor():
      game_over()
    if player.ycor() == trail8.ycor() and player.xcor() == trail8.xcor():
      game_over()
    if player.ycor() == trail9.ycor() and player.xcor() == trail9.xcor():
      game_over()
    if player.ycor() == trail10.ycor() and player.xcor() == trail10.xcor():
      game_over()
    if player.ycor() == trail11.ycor() and player.xcor() == trail11.xcor():
      game_over()
    if player.ycor() == trail12.ycor() and player.xcor() == trail12.xcor():
      game_over()
    if player.ycor() == trail13.ycor() and player.xcor() == trail13.xcor():
      game_over()
    if player.ycor() == trail14.ycor() and player.xcor() == trail14.xcor():
      game_over()
    if player.ycor() == trail15.ycor() and player.xcor() == trail15.xcor():
      game_over()
    if player.ycor() == trail16.ycor() and player.xcor() == trail16.xcor():
      game_over()
    if player.ycor() == trail17.ycor() and player.xcor() == trail17.xcor():
      game_over()
    if player.ycor() == trail18.ycor() and player.xcor() == trail18.xcor():
      game_over()
    if player.ycor() == trail19.ycor() and player.xcor() == trail19.xcor():
      game_over()
    if player.ycor() == trail20.ycor() and player.xcor() == trail20.xcor():
      game_over()
    if player.ycor() == trail21.ycor() and player.xcor() == trail21.xcor():
      game_over()
    if player.ycor() == trail22.ycor() and player.xcor() == trail22.xcor():
      game_over()
    if player.ycor() == trail23.ycor() and player.xcor() == trail23.xcor():
      game_over()
    if player.ycor() == trail24.ycor() and player.xcor() == trail24.xcor():
      game_over()
    if player.ycor() == trail25.ycor() and player.xcor() == trail25.xcor():
      game_over()

    #Player-Fake point collision
    if player.ycor() == fpoint1.ycor() and player.xcor() == fpoint1.xcor():
      game_over()

    #Player-Gate collision
    if player.ycor() == fpoint2.ycor() and player.xcor() == fpoint2.xcor():
      game_over()
    if player.ycor() == gate_en.ycor() and player.xcor() == gate_en.xcor():
      player.goto(gate_ex.xcor(),gate_ex.ycor())
