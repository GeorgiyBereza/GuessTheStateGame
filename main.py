import sys
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pointer = turtle.Turtle()
pointer.penup()
pointer.hideturtle()

states_data = pandas.read_csv("50_states.csv")
list_of_states = states_data["state"].to_list()

#for finding coordinates of states
# def get_moose_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_moose_click_coor)
# turtle.mainloop()

guessed_states = []
number_of_guessed_states = 0
while True:
    answer_state = screen.textinput(title=f"{number_of_guessed_states}/50 states guessed",
                                    prompt="What is the name of the state?").title()
    if answer_state == 'Exit':
        sys.exit()
    elif answer_state in list_of_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        number_of_guessed_states = len(guessed_states)
        x = states_data[states_data['state']== answer_state]['x'].values[0]
        y = states_data[states_data['state']== answer_state]['y'].values[0]
        pointer.goto(x,y)
        pointer.write(answer_state, font=("Verdana",
                                            8, "normal"),align='center')




