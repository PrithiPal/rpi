import LCD_1in44
import LCD_Config
import RPi.GPIO as GPIO

import time 

from PIL import Image,ImageDraw,ImageFont,ImageColor

TEMP_FILE='/sys/class/thermal/thermal_zone0/temp'


KEY_UP_PIN     = 6 
KEY_DOWN_PIN   = 19
KEY_LEFT_PIN   = 5
KEY_RIGHT_PIN  = 26
KEY_PRESS_PIN  = 13
KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16

#init GPIO
GPIO.setmode(GPIO.BCM) 
GPIO.cleanup()
GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Input with pull-up
GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY3_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up



def displayTemperature() : 
    LCD = LCD_1in44.LCD()


    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()
    
    image = Image.new("RGB", (LCD.width, LCD.height), "WHITE")
    draw = ImageDraw.Draw(image)
    
    x = 0
    y = 0

    while True : 

        image = Image.new("RGB", (LCD.width, LCD.height), "WHITE")
        draw = ImageDraw.Draw(image)

        tempFile = open(TEMP_FILE,'r')
        temp = int(tempFile.readline())/1000
        

        if GPIO.input(KEY_UP_PIN) == 0: # button is released       
            y=y-1
            
        if GPIO.input(KEY_LEFT_PIN) == 0: # button is released
            x=x-1
                    
            
        if GPIO.input(KEY_RIGHT_PIN) == 0: # button is released
            x=x+1

        if GPIO.input(KEY_DOWN_PIN) == 0: # button is released
            y=y+1


        draw.text((x,y), 'Temp : {} C'.format(str(temp)), fill = "BLUE")
        print('({},{})'.format(x,y))
        
        
        LCD.LCD_ShowImage(image,0,0)
        LCD_Config.Driver_Delay_ms(100)
        
    


if __name__ == '__main__':
    displayTemperature()