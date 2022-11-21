
#Snake by Gergoson (Except for everything stolen.)

from random import randint
import turtle
from time import sleep

delay = 0.2
timee = 0

#Window
wn = turtle.Screen()
wn.title("InsaniSnake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score 0", align="center", font=("Arial", 24, "normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, -280)
pen2.write("Nothing", align="center", font=("Arial", 24, "normal"))

#Score
score = 0

#Player
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("green")
player.penup()
player.goto(0,0)
movement_dir = "none"

#Point
point = turtle.Turtle()
point.shape("circle")
point.color("gold")
point.penup()
point.goto(0,40)

#Trail
trails = []

#Effects
effect = 'none'

#Functions
def player_up():
   global movement_dir
   if movement_dir != "d" and effect != 'Confusion':
    movement_dir = "u"
   elif movement_dir != "u" and effect == 'Confusion':
    movement_dir = "d"
  
def player_down():
   global movement_dir
   if movement_dir != "u" and effect != 'Confusion':
    movement_dir = "d"
   elif movement_dir != "d" and effect == 'Confusion':
    movement_dir = "u"

def player_right():
   global movement_dir
   if movement_dir != "l" and effect != 'Confusion':
    movement_dir = "r"
   elif movement_dir != "r" and effect == 'Confusion':
    movement_dir = "l"

def player_left():
   global movement_dir
   if movement_dir != "r" and effect != 'Confusion':
    movement_dir = "l"
   elif movement_dir != "l" and effect == 'Confusion':
    movement_dir = "r"

def move():
  if movement_dir == "u":
    y = player.ycor()
    player.sety(y + 20)
    
  if movement_dir == "d":
    y = player.ycor()
    player.sety(y - 20)
    
  if movement_dir == "r":
    x = player.xcor()
    player.setx(x + 20)
  
  if movement_dir == "l":
    x = player.xcor()
    player.setx(x - 20)

def game_over():
    for trail in trails:
     trail.goto(6900, 6900)

    trails.clear()

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
    pen.write("Game Over", align="center", font=("Arial", 80, "normal"))

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
    pen2.write("{}".format(dmessage), align="center", font=("Arial", 14, "italic"))

def trail_increase():
  new_trail = turtle.Turtle()
  new_trail.speed(0)
  new_trail.shape("square")
  new_trail.color("dark green")
  new_trail.penup()
  new_trail.goto(500,500)
  trails.append(new_trail)

def point_respawn():
    pr1 = randint(-7,7)
    pr2 = randint(-7,7)
    point.goto(pr1 * 40,pr2 * 40)

def eff_clear():
  global delay
  global wn
  global effect

  delay = 0.2
  wn.bgcolor('black')
  effect = 'none'

def effect_change():
  global delay
  global wn
  global effect

  eff_clear()
  eff_num = randint(1,7)
  if eff_num == 1:
    delay = 0.1
    effect = 'Speed'
  if eff_num == 2:
    effect = 'Catch!'
  if eff_num == 3:
    delay = 0.4
    effect = 'Slowness'
  if eff_num == 4:
    effect = 'Confusion'
  if eff_num == 5:
    trail_increase()
    effect = 'Growth'
  if eff_num == 6:
    trail_increase()
    trail_increase()
    effect = 'Double Growth'
  if eff_num == 7:
    delay = 0.06
    effect = 'Hyperspeed'



#Keyboard binding
wn.listen()
wn.onkeypress(player_up, "w")
wn.onkeypress(player_down, "s")
wn.onkeypress(player_left, "a")
wn.onkeypress(player_right, "d")
wn.onkeypress(point_respawn, "p")
wn.onkeypress(game_over, "g")

#Main game loop

while True:
  wn.update()

  timee += 1

  #Player-Wall collision
  if player.ycor() > 295:
   sleep(0.5)
   game_over()
  if player.ycor() < -295:
   sleep(0.5)
   game_over()
  if player.xcor() > 295:
   sleep(0.5)
   game_over()
  if player.xcor() < -295:
   sleep(0.5)
   game_over()

  #Point pickup
  if player.distance(point) < 20:
   score += 1
   pen.clear()
   pen.write("Score {}".format(score), align="center", font=("Arial", 24, "normal"))
   point_respawn()
   trail_increase()
   effect_change()
   pen2.clear()
   pen2.write("{}".format(effect), align="center", font=("Arial", 24, "normal"))
  
  #Move the end trails first in reverse order
  for index in range(len(trails)-1, 0, -1):
      x = trails[index-1].xcor()
      y = trails[index-1].ycor()
      trails[index].goto(x, y)

  #Move trail 0 to where the head is
  if len(trails) > 0:
      x = player.xcor()
      y = player.ycor()
      trails[0].goto(x,y)

  move()

  #Player-Trail collision
  for segment in trails:
      if segment.distance(player) < 20:
          sleep(0.5)
          game_over()

  if timee > 20 and effect == "Catch!":
    point_respawn()
    timee = 0


  sleep(delay)

