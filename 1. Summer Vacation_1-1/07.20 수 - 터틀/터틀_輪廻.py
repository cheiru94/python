# 제목 : 輪廻(윤회)

import turtle

kame = turtle.Turtle()

# 위치 잡기
for hosii in range(30) :
    
    kame.screen.bgcolor("BLACK")
    kame.color("PINK")
    kame.forward(1000)
    kame.right(145)
    kame.speed(0)
# 위치 안에서 돌기    
    for hosii in range(90) :
        kame.screen.bgcolor("BLACK")
        kame.color("PINK")
        kame.forward(500)
        kame.right(145)
        kame.speed(0)

turtle.done()