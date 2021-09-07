from turtle import*

bgcolor('black')
goto(0,-250)
speed(10)

def draw(a,b):
    pencolor(a)
    fillcolor(a)
    begin_fill()
    circle(b)
    end_fill()
    lt(90)
    fd(50)
    rt(90)

draw('red',250)
draw('white',200)
draw('red',150)
draw('blue',100)


rt(90)
goto(0,100)
pencolor('white')
fillcolor('white')
rt(18)
begin_fill()
for i in range(5):
    fd(190)
    lt(144)
end_fill()
hideturtle()
