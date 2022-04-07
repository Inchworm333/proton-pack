#!/usr/bin/python3
import gpiozero
import curses
from curses import wrapper

on_switch = gpiozero.LED(23)
shooting_mode = gpiozero.LED(22)
fire = gpiozero.LED(27)

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.noecho()

    # This raises ZeroDivisionError when i == 10.
    while(True):
        key = stdscr.getkey()
        if key == 'o':
            on_switch.toggle()
        if key == 's':
            shooting_mode.toggle()
        if key == 'f':
            fire.toggle()

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
