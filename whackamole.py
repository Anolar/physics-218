import RPi.GPIO as gpio
import time
import random

rounds = int(input('How many rounds to play? '))

score = 0

# Initialize I/O pins:

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

right_button = 24
gpio.setup(right_button, gpio.IN, gpio.PUD_UP)
        
mid_button = 23
gpio.setup(mid_button, gpio.IN, gpio.PUD_UP)

left_button = 25
gpio.setup(left_button, gpio.IN, gpio.PUD_UP)
        
rightled = 21
gpio.setup(rightled,gpio.OUT)
        
midled = 20
gpio.setup(midled,gpio.OUT)
        
leftled = 16
gpio.setup(leftled,gpio.OUT)

# Arrays to be indexed randomly
leds = [leftled, midled, rightled]
buttons = [left_button, mid_button, right_button]

# Main game loop
for i in range(0,rounds):

    # Gets current time, adds the length of the round to it.
    endtime = time.time()+.3
    # Random number to index LED and button arrays.
    side = random.randint(0,2)

    # Loop than runs each round. While system time is less than start time + round length
    while time.time()<endtime:

        # Sets the randomly determined LED high.
        gpio.output(leds[side],1)

        # If the correct button is pressed in time:
        if gpio.input(buttons[side]) == False:
            score+=1 # Increment Score
            print('Score:',score,'out of',rounds) # Prints score
            gpio.output(leds[side],0) # Set LED low.
            time.sleep(0.3) # Pause before begining next round.
            break # Begin next round

    # Set all LEDs Low.
    gpio.output(rightled,0)
    gpio.output(midled,0)
    gpio.output(leftled,0)


print(score, 'out of', rounds)

gpio.cleanup()
