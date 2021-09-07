import turtle
import random
import time
import sys

#SCREEN
s=turtle.Screen()
s.title('GAME')
s.bgcolor('blue')
#s.bgpic('bg6.gif')
s.tracer(0)

dlt=turtle.Turtle()



#RUNNER
t=turtle.Turtle()
t.color('red')
t.shape('circle')
t.penup()

#SCORE
r=turtle.Turtle()
r.color('#edff00')
r.speed(1)
r.penup()
r.goto(-330,250)
r.write('Score :',move=False,font=('impact',20,'normal'),align='left')
r.hideturtle()
r.hideturtle()


#GOAL
g=turtle.Turtle()
g.color('#9f0bd8')
g.shape('circle')
g.penup()
g.a=random.randint(-315,315)
g.b=random.randint(-255,235)
g.goto(g.a,g.b)
(g.a,g.b)=g.pos()


#deadline
dlt.speed(0)
dlt.pensize(5)
dlt.penup()
dlt.fillcolor('#54e041')
dlt.begin_fill()
dlt.goto(-320,240)
dlt.pendown()
dlt.goto(320,240)
dlt.goto(320,-260)
dlt.goto(-320,-260)
dlt.goto(-320,240)
dlt.end_fill()
dlt.penup()
dlt.ht()


t.key=''
t.score=0
t.d=2
delay=0.01




def funup():
    t.key='up'
def fundown():
    t.key='down'
def funright():
    t.key='right'
def funleft():
    t.key='left'

s.listen()
s.onkeypress(funup,'Up')
s.onkeypress(fundown,'Down')
s.onkeypress(funright,'Right')
s.onkeypress(funleft,'Left')

def move():
    x=t.xcor()
    y=t.ycor()
    if t.key=='up':
        t.sety(y+t.d)
    if t.key=='down':
        t.sety(y-t.d)
    if t.key=='right':
        t.setx(x+t.d)
    if t.key=='left':
        t.setx(x-t.d)


def do():
    r.undo()
    t.score+=1
    r.goto(-240,250)
    r.write(t.score,font=('arial',20,'bold'),align='left')
    g.a=random.randint(-315,315)
    g.b=random.randint(-255,235)
    g.goto(g.a,g.b)

c=(g.pos()-t.pos())
def target():
    if c[0] > -10 and c[0] < 10 and c[1] > -10 and c[1] < 10:
        do()
 
def gameover():
    for i in range(1,50):
        time.sleep(0.01)
        dlt.write('GAME OVER',font=('impact',i,'normal'),align='center')
        dlt.undo()


def deadline():
    if dl[0] < -320 or dl[0] > 320 or dl[1] < -260 or dl[1] > 240:
        dlt.color('red')
        dlt.goto(0,0)
        gameover()
        time.sleep(5)
        dlt.ht()
        sys.exit()

def lup():
    for j in range(1,70,4):
        dlt.goto(0,0)
        time.sleep(0.01)
        dlt.pencolor('green')
        dlt.write('Speed Up',font=('impact',j,'normal'),align='center')
        dlt.undo()
        dlt.ht()
t.lp=0
def lvl():
    if t.score >=5 and t.score <10:
        if t.lp==0:
            lup()
            t.lp=1
            t.d=3
    elif t.score >=10 and t.score <20:
        if t.lp==1:
            lup()
            t.lp=2
            t.d=4
    elif t.score >=20  and t.score <30:
        if t.lp==2:
            lup()
            t.lp=3
            t.d=5
    elif t.score >=30:
        if t.lp==3:
            lup()
            t.lp=4
            t.d=6
    


while True:
    dl=t.pos()
    time.sleep(delay)
    deadline()
    move()
    s.update()
    target()
    c=g.pos()-t.pos()
    lvl()

s.mainloop()



