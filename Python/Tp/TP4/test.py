import png
import turtle

rows = [
    (255,0,0, 0,255,0, 0,0,255),
    (128,0,0, 0,128,0, 0,0,128)
    ]
image = png.from_array(rows, "RGB")
image.save("swatch.png")

list = [[222],[898]]
for i in range(len(list[0])):
    print(list[0][i])

turtle.setup(900,900)
turtle.bgpic('maze1.png')
turtle.title('Maze')
turtle.pencolor('green')
turtle.shape('turtle')


turtle.down()
turtle.goto(20,0)
turtle.up

turtle.exitonclick()


