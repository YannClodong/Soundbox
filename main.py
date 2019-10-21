import RPi.GPIO as GPIO
import playsound as p
import loadInfos as l
import time as t

(buttons, sounds) = l.load()

highState = True

for button in buttons:
    GPIO.setup(button, GPIO.IN)

while True:
    for i in range(len(buttons)):
        button = buttons[i]
        if(GPIO.input(button) == highState):
            p.playsound(sounds[i])
        while(GPIO.input(button) == highState):
            print("")
    t.sleep(.1)