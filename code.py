'''
ESC204 2022W Widget Lab 1, Part 10
Task: Blink the Pico's onboard LED.
Author: Cathy Feng, Melanie Wang
'''
# Import libraries needed for blinking the LED
import board
import digitalio
import time

# Configure the internal GPIO connected to the red as a digital output
led_red = digitalio.DigitalInOut(board.GP17)
led_red.direction = digitalio.Direction.OUTPUT

# Configure the internal GPIO connected to the green as a digital output
led_gre = digitalio.DigitalInOut(board.GP13)
led_gre.direction = digitalio.Direction.OUTPUT

# Configure the internal GPIO connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Sets the internal resistor to pull-up

# Print a message on the serial console
print('Hello! My LED is blinking now.')

x = 0

# Loop so the code runs continuously
while True:
    #button.value=true if unpressed
    if (((not button.value) and x==0) or (x==1 and button.value)): #if the button is pressed for the 1st time
        x=1
        led_red.value = True
        led_gre.value = False
        time.sleep(0.5)
        led_red.value = False   # Turn off the LED
        led_gre.value = False   # Turn off the LED
        time.sleep(0.5)
        print("state1")
    elif (((not button.value) and x==1) or (x==2 and button.value)): #if the button is pressed for the 2nd time
        x=2
        led_red.value = True
        led_gre.value = True
        time.sleep(0.5)
        led_red.value = False   # Turn off the LED
        led_gre.value = False   # Turn off the LED
        time.sleep(0.5)
        print("state2")
    elif (((not button.value) and x==2) or (x==0 and button.value)): #if the button is pressed for the 3rd time
        x=0
        led_red.value = False   # Turn off the LED
        led_gre.value = False   # Turn off the LED
        time.sleep(0.5)
        print("state0")

