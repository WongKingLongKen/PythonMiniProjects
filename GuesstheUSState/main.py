import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
if answer_state:
    answer_state = answer_state.title()

while answer_state and answer_state != "Exit":
    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    elif answer_state not in states:
        print("That's not a state name.")
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?")
    # the case for clicking Cancel and hence answer_state becomes None 
    if answer_state:
        answer_state = answer_state.title()

missing_states = [state for state in states if state not in guessed_states]
new_data = pd.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")

screen.exitonclick()



