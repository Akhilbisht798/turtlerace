import turtle as t
import random



is_raceon = False
screen = t.Screen()
screen.setup(width = 500, height= 400)
user_input= screen.textinput(title = "Make your Bet",prompt = "Which turtle won the Race. Enter a color: " )
colour = ["violet","indigo","blue","green","yellow","orange","red"]
turtle_list = []
y_coord = 180
for turtle_ind in range(7):
    tim = t.Turtle()
    tim.color(colour[turtle_ind])
    tim.shape("turtle")
    tim.penup()
    tim.goto(x= -230, y = y_coord)
    y_coord -= 50
    turtle_list.append(tim)

if user_input:
    is_raceon = True
while is_raceon:
    for i in turtle_list:
        movement = random.randint(0,10)
        i.forward(movement)
        if i.xcor()>230:
            is_raceon = False
            winner = i.pencolor()
            if user_input == winner:
                print(f"you won. Winng color is {winner}")
            else:
                print(f"you lost. Winner is {winner}")

            




screen.exitonclick()
