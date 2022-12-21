
#Snake by Gergoson (Except for everything stolen.)

from random import randint
import turtle
from time import sleep

delay = 0.2
timee = 0
devmode = False

#Window
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#Pen
spen = turtle.Turtle()
spen.speed(0)
spen.shape("square")
spen.color("white")
spen.penup()
spen.hideturtle()
spen.goto(0, 255)
spen.write("Score: 0", align="center", font=("Arial", 24, "normal"))

epen = turtle.Turtle()
epen.speed(0)
epen.shape("square")
epen.color("white")
epen.penup()
epen.hideturtle()
epen.goto(0, -290)
epen.write("Nothing", align="center", font=("Arial", 24, "normal"))

if devmode == True:
  tpen = turtle.Turtle()
  tpen.speed(0)
  tpen.shape("square")
  tpen.color("white")
  tpen.penup()
  tpen.hideturtle()
  tpen.goto(270, 270)
  tpen.write("0", align="center", font=("Arial", 12, "normal"))

hspen= turtle.Turtle()
hspen.shape("square")
hspen.color("white")
hspen.penup()
hspen.hideturtle()
hspen.goto(0,240)
hspen.write("High Score: 0", align="center", font=("Arial", 14, "normal"))

#Score
score = 0
hscore = 0

#Player
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("green")
player.penup()
player.goto(0, 0)
movement_dir = "none"
alive = True

#Point
point = turtle.Turtle()
point.shape("circle")
point.color("gold")
point.penup()
point.goto(0,40)
pointbxy = 0
pointbdir = 'u'

#Mimics
mimics = []

#Mines
mines = []

mine_time = False
camo_time = False

#Portals
portalb = turtle.Turtle()
portalb.shape("circle")
portalb.color("blue")
portalb.penup()
portalb.goto(0,800)

portalo = turtle.Turtle()
portalo.shape("circle")
portalo.color("orange")
portalo.penup()
portalo.goto(0,800)

portalr = turtle.Turtle()
portalr.shape("circle")
portalr.color("red")
portalr.penup()
portalr.goto(0,800)

portalg = turtle.Turtle()
portalg.shape("circle")
portalg.color("dark blue")
portalg.penup()
portalg.goto(0,800)

#Outline
outline = turtle.Turtle()
outline.shape("square")
outline.color("white")
outline.penup()
outline.goto(291, 291)
outline.pendown()
outline.goto(-291, 291)
outline.goto(-291, -291)
outline.goto(291, -291)
outline.goto(291, 291)
outline.penup()
outline.goto(0, 800)

#Trails
trails = []

#Effects
effect = 'Nothing'

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

def eff_clear():
  global delay
  global effect
  global timee

  timee = 0
  delay = 0.2
  effect = 'Nothing'
  for mimic in mimics:
    mimic.goto(6900, 9600)
  for trail in trails:
    trail.color('dark green')
  for mine in mines:
    mine.goto(9600, 6900)
  portalb.goto(0, 800)
  portalo.goto(0, 800)
  portalr.goto(0, 800)
  portalg.goto(0, 800)
  mimics.clear()
  mines.clear()

def game_over():
    global movement_dir
    global score
    global alive
    global hscore


    alive = False
    for trail in trails:
     trail.goto(6900, 6900)
    trails.clear()
    for mimic in mimics:
      mimic.goto(6900, 9600)
    for mine in mines:
      mine.goto(6900, 9600)
    mimics.clear()
    mines.clear()
    movement_dir = "ass"
    player.goto(800,800)
    point.goto(800,800)
    spen.clear()
    eff_clear()
    epen.clear()
    outline.clear()
    hspen.clear()

    wn.update()
    wn.bgcolor("dark red")
    gpen = turtle.Turtle()
    gpen.speed(0)
    gpen.shape("square")
    gpen.color("red")
    gpen.penup()
    gpen.hideturtle()
    gpen.goto(0, 0)
    gpen.write("Game Over", align="center", font=("Arial", 80, "normal"))

    dmv = randint(1,16)
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
    if dmv == 12:
      dmessage = "There aren't even any words to describe how bad you are."
    if dmv == 13:
      dmessage = 'Do you not have anything better to do?'
    if dmv == 14:
      dmessage = "You cannot win, no, seriously, it's not possible."
    if dmv == 15:
      dmessage = "Tip: Give up."
    if dmv == 15:
      dmessage = "Tip: You can't lose if you exit the game."
    if dmv == 16:
      dmessage = "Tip: Think, but I doubt you can even do that."
    dmpen = turtle.Turtle()
    dmpen.speed(0)
    dmpen.shape("square")
    dmpen.color("red")
    dmpen.penup()
    dmpen.hideturtle()
    dmpen.goto(0,-20)
    dmpen.write("{}".format(dmessage), align="center", font=("Arial", 14, "italic"))

    rpen = turtle.Turtle()
    rpen.speed(0)
    rpen.shape("square")
    rpen.color("red")
    rpen.penup()
    rpen.hideturtle()
    rpen.goto(0,-280)
    rpen.write("Restarting in 3 seconds.", align="center", font=("Arial", 16, "normal"))
    wn.update()
    rpen.clear()
    sleep(1)
    rpen.write("Restarting in 2 seconds.", align="center", font=("Arial", 16, "normal"))
    wn.update()
    rpen.clear()
    sleep(1)
    rpen.write("Restarting in 1 seconds.", align="center", font=("Arial", 16, "normal"))
    wn.update()
    rpen.clear()
    sleep(1)

    gpen.clear()
    dmpen.clear()
    rpen.clear()
    wn.bgcolor('black')
    
    if score > hscore:
      hscore = score
    hspen.write("High Score: {}".format(hscore), align="center", font=("Arial", 14, "normal"))
    score = 0

    eff_clear()
    player.goto(0, 0)
    point.goto(0, 40)
    spen.write("Score: 0", align="center", font=("Arial", 24, "normal"))
    epen.write("Nothing", align="center", font=("Arial", 24, "normal"))
    outline.penup()
    outline.goto(291,291)
    outline.pendown()
    outline.goto(-291,291)
    outline.goto(-291,-291)
    outline.goto(291,-291)
    outline.goto(291,291)
    outline.penup()
    outline.goto(0,800)
    alive = True

def trail_increase():
  new_trail = turtle.Turtle()
  new_trail.speed(0)
  new_trail.shape("square")
  new_trail.color("dark green")
  new_trail.penup()
  new_trail.goto(500,500)
  trails.append(new_trail)

def point_respawn():
  point.goto(randint(-14,14) * 20, randint(-14,14) * 20)

def mimic_spawn():
  mimic = turtle.Turtle()
  mimic.shape("circle")
  mimic.color("yellow")
  mimic.penup()
  mimic.goto(randint(-7,7) * 40, randint(-7,7) * 40)
  mimics.append(mimic)

def mine_spawn():
  mine = turtle.Turtle()
  mine.shape("square")
  mine.color("red")
  mine.penup()
  mine.goto(randint(-7,7) * 40, randint(-7,7) * 40)
  mines.append(mine)

def portal_respawn():
  portalb.goto(randint(-7,7) * 40, randint(-7,7) * 40)
  portalo.goto(randint(-7,7) * 40, randint(-7,7) * 40)

def portal2_respawn():
  portalr.goto(randint(-7,7) * 40, randint(-7,7) * 40)
  portalg.goto(randint(-7,7) * 40, randint(-7,7) * 40)

def point_bounce():
  global pointbdir

  if pointbxy == 0 and pointbdir == 'u':
    x = point.xcor() + 19.9999999 #Fix for not picking up the point when going the opposite direction, I know it's bad.
    if x > 280:
      pointbdir = 'd'
    else:
      point.setx(x)
  if pointbxy == 0 and pointbdir == 'd':
    x = point.xcor() - 19.999999
    if x < -280:
      pointbdir = 'u'
    else:
      point.setx(x)
  if pointbxy == 1 and pointbdir == 'u':
    y = point.ycor() + 19.999999
    if y > 280:
      pointbdir = 'd'
    else:
      point.sety(y)
  if pointbxy == 1 and pointbdir == 'd':
    y = point.ycor() - 19.999999
    if y < -280:
      pointbdir = 'u'
    else:
      point.sety(y)

def effect_change():
  global delay
  global effect
  global mine_time
  global camo_time
  global score
  global pointbxy
  if effect == 'Hyperspeed' or effect == 'Double Growth' or effect == ' Triple Mimics' or effect == 'Catch!' or effect == 'Bouncing':
    score += 5
  if effect == 'Confusion' or effect == 'Mega Growth' or effect == 'Mimic Swarm' or effect == 'Minefield' or effect == 'Camouflage':
    score += 10
  if effect == 'Double Portals' or effect == 'Boundryless':
    score -= 5
  if effect == 'No Points':
    score -= 10
  if effect == 'Bonus Points':
    score += 20

  eff_clear()
  eff_num = randint(0,23)
  if eff_num == 1:
    delay = 0.1
    effect = 'Speed'

  if eff_num == 2:
    effect = 'Catch!'

  if eff_num == 3:
    delay = 0.4
    effect = 'Slowness'

  if eff_num == 4:
    delay = 0.16
    effect = 'Confusion'

  if eff_num == 5:
    trail_increase()
    effect = 'Growth'

  if eff_num == 6:
    trail_increase()
    trail_increase()
    effect = 'Double Growth'

  if eff_num == 7:
    trail_increase()
    trail_increase()
    trail_increase()
    trail_increase()
    effect = 'Mega Growth'

  if eff_num == 8:
    delay = 0.05
    effect = 'Hyperspeed'

  if eff_num == 9:
    mimic_spawn()
    mimic_spawn()
    effect = 'Mimics'

  if eff_num == 10:
    mine_spawn()
    mine_spawn()
    mine_time = True
    effect = 'Mines'

  if eff_num == 11:
    effect = 'Acceleration'

  if eff_num == 12:
    score += 5
    effect = 'Deceleration'

  if eff_num == 13:
    effect = 'Bonus Points'

  if eff_num == 14:
    effect = 'No Points'

  if eff_num == 15:
    portal_respawn()
    effect = 'Portals'

  if eff_num == 16:
    portal_respawn()
    portal2_respawn()
    effect = 'Double Portals'

  if eff_num == 17:
    effect = 'Boundryless'
  
  if eff_num == 18:
    pointbxy = randint(0, 1)
    effect = 'Bouncing'
  
  if eff_num == 19:
    effect = 'No Growth'
  
  if eff_num == 20:
    mimic_spawn()
    mimic_spawn()
    mimic_spawn()
    effect = 'Triple Mimics'
  
  if eff_num == 21:
    mimic_spawn()
    mimic_spawn()
    mimic_spawn()
    mimic_spawn()
    mimic_spawn()
    effect = 'Mimic Swarm'

  if eff_num == 22:
    mine_spawn()
    mine_spawn()
    mine_spawn()
    mine_spawn()
    mine_spawn()
    mine_time = True
    effect = 'Minefield'
  
  if eff_num == 23:
    camo_time = True
    effect = 'Camouflage'


  spen.clear()
  spen.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))

#Keyboard binding
wn.listen()
wn.onkeypress(player_up, "w")
wn.onkeypress(player_down, "s")
wn.onkeypress(player_left, "a")
wn.onkeypress(player_right, "d")

#Main game loop
while alive == True:
  wn.update()
  
  #Player-Wall collision
  if player.ycor() > 295 and effect != 'Boundryless':
    sleep(0.5)
    game_over()
  elif player.ycor() > 295 and effect == 'Boundryless':
    player.sety(-280)

  if player.ycor() < -295 and effect != 'Boundryless':
    sleep(0.5)
    game_over()
  elif player.ycor() < -295 and effect == 'Boundryless':
    player.sety(280)
  
  if player.xcor() > 295 and effect != 'Boundryless':
    sleep(0.5)
    game_over()
  elif player.xcor() > 295 and effect == 'Boundryless':
    player.setx(-280)
  
  if player.xcor() < -295 and effect != 'Boundryless':
    sleep(0.5)
    game_over()
  elif player.xcor() < -295 and effect == 'Boundryless':
    player.setx(280)

  #Player-Mimic collision
  for mimic in mimics:
    if mimic.distance(player) < 20:
      sleep(0.5)
      game_over()

  #Player-Mine collision
  for mine in mines:
    if mine.distance(player) < 20:
      sleep(0.5)
      game_over()

  #Portal-Player collision
  if player.distance(portalb) < 20:
    player.goto(portalo.xcor(),portalo.ycor())

  elif player.distance(portalo) < 20:
    player.goto(portalb.xcor(),portalb.ycor())

  if player.distance(portalr) < 20:
    player.goto(portalg.xcor(),portalg.ycor())
  
  elif player.distance(portalg) < 20:
    player.goto(portalr.xcor(),portalr.ycor())

  #Point pickup
  if player.distance(point) < 20:
   score += 10
   spen.clear()
   spen.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))
   point_respawn()
   effect_change()
   if effect != 'No Growth':
    trail_increase()
   epen.clear()
   epen.write("{}".format(effect), align="center", font=("Arial", 24, "normal"))

  timee += 1

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
  if effect == 'Bouncing':
    point_bounce()

  #Player-Trail collision
  for trail in trails:
      if trail.distance(player) < 20:
          sleep(0.5)
          game_over()


  #Timers
  if timee > 20 and effect == "Catch!":
    point_respawn()
    timee = 0
  
  if timee > 5 and mine_time == True:
    for mine in mines:
      mine.shapesize(0.01,0.01,0.01)
    timee = 0
    mine_time = False

  if timee > 4 and camo_time == True:
    for trail in trails:
      trail.color('black')
    timee = 0
    camo_time = False
  
  #Speed effects
  if effect == 'Acceleration':
    delay /= 1.02
  if effect == 'Deceleration':
    delay *= 1.02

  if devmode == True:
   tpen.clear()
   tpen.write("{}".format(timee), align="center", font=("Arial", 12, "normal"))

  wn.update() #I know there are two of these but I can't bother coming up with a better fix for the imput lag.


  sleep(delay)  #This took me an embarrisingly long time to do because I accidently imported the wrong thing.


