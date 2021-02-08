from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)



val = 0
while True:
    led.value = val%1  # off
    sleep(0.05)
    val=val+0.1
