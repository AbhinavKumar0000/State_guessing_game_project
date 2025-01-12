import pandas as bhalu
from turtle import Turtle, Screen

screen = Screen()
kachua = Turtle()

screen.title("Indian States")
image = "India-state.gif"
screen.addshape(image)
kachua.shape(image)


data = bhalu.read_csv("C:/Users/abhin/PycharmProjects/day-25-start/State_guessing_game/states_data.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 states correct", prompt="What's another state's name ?")
    print(answer_state)
    if answer_state == "Exit":
        missing_states = [states for states in all_states if states not in guessed_states]
        new_data = bhalu.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


    if answer_state in all_states:
        guessed_states.append(answer_state)
        k = Turtle()
        k.hideturtle()
        k.penup()
        state_data = data[data.state == answer_state]
        xcor = int(state_data.x.iloc[0])
        ycor = int(state_data.y.iloc[0])
        k.goto(xcor,ycor)
        k.write(answer_state)






screen.exitonclick()