"""
File: MidpointKarel.py
Name: SWLYU
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    put beeper, go touch wall, put beeper, turn around, go back, on beeper, pick beeper, turn around, move, put beeper.
    repeat, such as: 1->7 ; 2->6 ; 3->5 ; 4
    the mid-point will have 2 beepers, go back on beeper, pick 1 beeper.
    """
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
            turn_around()
            move()
            put_beeper()
    turn_around()
    while not on_beeper():
        move()
    pick_beeper()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
