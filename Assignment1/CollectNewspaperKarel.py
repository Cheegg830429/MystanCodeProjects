"""
File: CollectNewspaperKarel.py
Name: SWLYU
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at (3,4), will go to (6,3), and pick up the newspaper, facing East.
    Post-condition: Karel go back to (3,4) from (6,3), facing East, and put down the newspaper.
    """
    move_to_beeper()
    go_back()


def move_to_beeper():
    """
    Pre-condition: Karel is at (3,4), facing East.
    Post-condition: Karel is at (6,3), and pick up the newspaper, facing East.
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def go_back():
    """
    Pre-condition: Karel is at (6,3), and pick up the newspaper, facing East.
    Post-condition: Karel go back to (3,4) from (6,3), facing East, and put down the newspaper.
    """
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
    put_beeper()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
