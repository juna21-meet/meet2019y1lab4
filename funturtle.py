import turtle
turtle.shape('square')
turtle.shape('turtle')
finn=turtle.clone()
finn.shape('square')
finn.goto(100,100)
finn.goto(200,100)
finn.goto(200,0)
finn.goto(100,0)
finn.goto(100,100)

charlie=turtle.clone()
charlie.shape('triangle')
charlie.penup()
charlie.goto(-100,0)
charlie.pendown()
charlie.goto(-100,100)
turtle.mainloop()


