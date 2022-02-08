import turtle
import add_state as s
import pandas

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
img = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(img)
turtle.shape(img)
new_state = s.State()
user_guesses = []
missing_states = []

playing = True
while playing:
    if new_state.correct_answers == 0:
        user_guess = screen.textinput("Guess the State", "Please try and guess a state").title()
    elif new_state.correct_answers == 50:
        new_state.end_game()
        playing = False
    else:
        user_guess = screen.textinput(f"{new_state.correct_answers}/50 States Correct",
                                      "Please try and guess a state").title()
        if user_guess in states:
            user_guesses.append(user_guess)
            state = data[data.state == user_guess]
            x_cor = int(state.x)
            y_cor = int(state.y)
            print(f"{x_cor}, {y_cor}")
            new_state.move_to_location(u_input=user_guess, x=x_cor, y=y_cor)
        elif user_guess == "Exit":
            states_to_learn = [state for state in states if state not in user_guesses]
            # for i in states:
            #     if i not in user_guesses:
            #         missing_states.append(i)
            #     else:
            #         pass
            new_data = pandas.DataFrame(states_to_learn, columns=["States"])
            new_data.to_csv("states_to_learn2.csv")
            break

screen.exitonclick()

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
