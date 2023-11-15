"""
File: StoneMasonKarel.py
Name: SWLYU
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Turn left, go up, if no beeper, put beeper, if not front_is_clear, go back, facing east.
    move four times, and repeat the function mentioned above, until touch the wall.
    """
    go_put_beepers()
    while front_is_clear():
        move_four_times()
        go_put_beepers()


def go_put_beepers():
    """
    Turn left, go up, if no beeper, put beeper, if not front_is_clear, go back, facing east.
    """
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if on_beeper():
        turn_around()
    else:
        put_beeper()
        turn_around()

    while front_is_clear():
        move()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def move_four_times():
    for i in range(4):
        move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
