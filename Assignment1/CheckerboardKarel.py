"""
File: CheckerboardKarel.py
Name: SWLYU
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    1*8: facing east, put beeper, while front is clear, move, if front clear, move, put beeper, until wall, go back.
    2*8: turn right (facing north), while front is clear, and if on beeper, move, turn right (east), and fill one line.
    3*8: if not on beeper, move, put beeper, turn right, and fill one line.
    8*1: (north) if not front is clear, turn left (facing north), check clear, move, fill one line.
    """
    fill_one_line()
    while front_is_clear():
        if on_beeper():
            move()
            turn_right()
            if front_is_clear():
                move()
                fill_one_line()
            else:
                turn_left()
                if front_is_clear():
                    move()
                    turn_right()
                    fill_one_line()
        else:
            move()
            turn_right()
            fill_one_line()


def fill_one_line():
    """
    1*8: facing east, put beeper, while front is clear, move, if front clear, move, put beeper, until wall, go back.
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    go_back()
    turn_right()


def go_back():
    turn_around()
    while front_is_clear():
        move()


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
