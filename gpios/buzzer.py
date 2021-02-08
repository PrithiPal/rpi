import RPi.GPIO as GPIO
from gpiozero import LED
import time

buzzer_pin = 12

def setup():
    # Remove warning message
    GPIO.setwarnings(False)
    # Set the pin mode to BOARD mode
    GPIO.setmode(GPIO.BOARD)
    # Set the touch button to input mode
    GPIO.setup(buzzer_pin,GPIO.OUT)


def buzzer() : 

    MAX_FREQ = 20000
    initFreq = 100
    initDuty = 50

    INCREMENT = 50
    UP = 1
    
    buzz = GPIO.PWM(buzzer_pin,initFreq)
    buzz.start(initDuty)
    
    while True : 
        
        print("({},{})".format(initFreq,initDuty))
        time.sleep(0.0005)
        
        if(initFreq == MAX_FREQ) : 
            UP = 0
        
        if(initFreq == 0) : 
            UP = 1
        
        
        if(UP) : 
            initFreq = initFreq + INCREMENT
        else:
            initFreq = initFreq - INCREMENT
        
        if(initFreq == 0) : 
            buzz.ChangeFrequency(initFreq+10)
        else : 
            buzz.ChangeFrequency(initFreq)
        


if __name__ == '__main__':
    setup()
    buzzer()
