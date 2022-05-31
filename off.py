#!/usr/bin/python3
import gpiozero

i = 0 

while i <= 23:
    led = gpiozero.LED(i)
    i = i + 1
