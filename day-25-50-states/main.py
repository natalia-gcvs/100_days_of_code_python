import turtle
import pandas as pd
from pascal_case_converter import Answer
from state import State

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
screen.listen()

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# screen.onscreenclick(get_mouse_click_coor)
#
# screen.mainloop()

states = pd.read_csv('50_states.csv')
states_guessed = []
states_to_learn = []
while len(states_guessed) < 2:
    answer = Answer(len(states_guessed))
    answer_converted = answer.converter()
    for index, state in enumerate(states['state']):
        if state == answer_converted:
            states_guessed.append(state)
            state_class = State(states["x"][index], states["y"][index], state)

    if answer_converted == 'Exit':
        turtle.bye()
        for state in states['state']:
            if state not in states_guessed:
                states_to_learn.append(state)
        missing_states = pd.DataFrame(states_to_learn)
        missing_states.to_csv('missing_states.csv')
turtle.bye()


