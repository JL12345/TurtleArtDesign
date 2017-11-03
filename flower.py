def flower(t,c,x,y):
    t.width(3)
    for times in range(20):
        t.color(c)
        t.penup()
        t.goto(0,0)
        t.forward(75)
        t.pendown()
        t.right(10)
        t.penup()
        t.goto(x,y)
        t.pendown()
        for times in range(20):
                t.forward(75)
                t.right(91)
