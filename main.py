import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv("50_states.csv")

states_guessed = []
while len(states_guessed) < 50:
    answer = screen.textinput(f"{len(states_guessed)}/50 States Correct", "What's another state's name?").title()
    user_state = states[states.state == answer]
    if len(user_state) and answer not in states_guessed:
        states_guessed.append(answer)
        pointer = turtle.Turtle()
        pointer.hideturtle()
        pointer.penup()
        pointer.goto(int(user_state.x), int(user_state.y))
        pointer.write(answer, align="center")

    if answer == "Exit":
        missing_states = []
        for state in states.state.to_list():
            if state not in states_guessed:
                missing_states.append(state)
        pd.DataFrame(missing_states).to_csv("missing_states.csv")
        break
