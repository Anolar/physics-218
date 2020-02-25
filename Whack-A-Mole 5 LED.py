import RPi.GPIO as gpio
import time
import random

rounds = int(input('How many rounds to play? '))

score = 0

# Initialize I/O pins:

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

#Button and LED nubmers from 0-4, left to right.
button0 = 5
gpio.setup(button0, gpio.IN, gpio.PUD_UP)
        
button1 = 6
gpio.setup(button1, gpio.IN, gpio.PUD_UP)

button2 = 13
gpio.setup(button2, gpio.IN, gpio.PUD_UP)

button3 = 19
gpio.setup(button3, gpio.IN, gpio.PUD_UP)

button4 = 26
gpio.setup(button4, gpio.IN, gpio.PUD_UP)
        
led0 = 25
gpio.setup(led0,gpio.OUT)
        
led1 = 12
gpio.setup(led1,gpio.OUT)

led2 = 16
gpio.setup(led2,gpio.OUT)

led3 = 20
gpio.setup(led3,gpio.OUT)

led4 = 21
gpio.setup(led4,gpio.OUT)

# Lists to be indexed randomly
leds = [led0, led1, led2, led3, led4]
buttons = [button0, button1, button2, button3, button4]

# Main game loop
for i in range(0,rounds):

    # Gets current time, adds the length of the round to it.
    endtime = time.time()+0.3
    # Random number to index LED and button arrays.
    side = random.randint(0,4)

    # Loop than runs each round. While system time is less than start time + round length
    while time.time()<endtime:

        # Sets the randomly determined LED high.
        gpio.output(leds[side],1)

        # If the correct button is pressed in time:
        if gpio.input(buttons[side]) == False:
            score+=1 # Increment Score
            print('Score:',score,'out of',rounds) # Prints score
            gpio.output(leds[side],0) # Set LED low.
            time.sleep(endtime-time.time()) # Pause before begining next round.
            break # Begin next round

    # Set all LEDs Low.
    gpio.output(led0,0)
    gpio.output(led1,0)
    gpio.output(led2,0)
    gpio.output(led3,0)
    gpio.output(led4,0)

print(score, 'out of', rounds)

gpio.cleanup()