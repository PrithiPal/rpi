import RPi.GPIO as GPIO
from gpiozero import LED
import picamera
import time

Infrared = 7   #7
tmp = 0
i = 0
led = 11

def setup():
    # Remove warning message
    GPIO.setwarnings(False)
    # Set the pin mode to BOARD mode
    GPIO.setmode(GPIO.BOARD)
    # Set the touch button to input mode
    GPIO.setup(Infrared,GPIO.IN)
    GPIO.setup(led,GPIO.OUT)


def Print(x):
    global tmp, i
    if x != tmp:
        if x == 1:
            print('**********')
            print('* !YES! *')
            print('**********')
            GPIO.output(led,1)

            i += 1
        if x == 0:
            print('**********')
            print('* !NO! *')
            print('**********')
            GPIO.output(led,0)
        tmp = x


if __name__ == '__main__':
    setup()

    try:
        while True:
            Print(GPIO.input(Infrared))
    except KeyboardInterrupt:
        # Capture keyboard^C to exit the program
        print('You terminated the program\nThe program ends!')
        GPIO.cleanup()


