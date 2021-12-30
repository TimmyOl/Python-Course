# Copyright 2021 Timmy Olsson
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Quiz")
background_image = "./blank_states_img.gif"
screen.addshape(background_image)

turtle.shape(background_image)

correct = 0
guessed_states = []

game_on = True

def set_name_and_pont(x, y):
    """Print the name on the state on the map and give 1 point for correct answer

    Args:
        x (int): x coordinate on the map
        y (int): y coordinate on the map
    """
    global correct
    global answer_state
    global guessed_states
    if answer_state not in guessed_states:
        correct += 1
        guessed_states.append(answer_state)
        text = turtle.Turtle()
        text.hideturtle()
        text.color("#000")
        text.penup()
        text.goto(x=x, y=y)
        text.write(answer_state, move=False, font=("arial", 12, "normal"), align="center")
        text.pendown()

while game_on:
    #Create a textbox for guessing
    answer_state = screen.textinput(title=f"{correct}/50, Guess the state", prompt="What's another states name?")

    #Load states from csv
    states = pandas.read_csv("./50_states.csv")

    #Find answer_state in states data frame if it exists
    for idx, row in states.iterrows():
        if row["state"] == answer_state:
            set_name_and_pont(x=row["x"], y=row["y"])

    #Win check
    if correct == 50:
        text = turtle.Turtle()
        text.hideturtle()
        text.color("#000")
        text.penup()
        text.goto(x=0, y=0)
        text.write("YOU WON!", move=False, font=("arial", 50, "bold"), align="center")
        text.pendown()
        game_on = False

turtle.mainloop()
# screen.exitonclick()
