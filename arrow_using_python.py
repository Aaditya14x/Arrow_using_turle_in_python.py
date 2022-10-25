from turtle  import* 
from random import randint
speed(0)
bgcolor("white")
X = 1
while X < 5:
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colormode(255)
    pencolor(r,g,b)
    fd(10+X)
    
    X+=1
    exitonclick


