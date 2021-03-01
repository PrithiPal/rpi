import LCD_1in44
import LCD_Config
import sys 
from PIL import Image,ImageDraw,ImageFont,ImageColor
import textwrap
import random 
import time

def main(display_string):
    LCD = LCD_1in44.LCD()
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R

    image = Image.new("RGB", (LCD.width, LCD.height), "WHITE")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 10)

    margin = offset = 5
    for line in textwrap.wrap(display_string, width=20):
        draw.text((margin, offset), line, font=font, fill="BLACK")
        offset += font.getsize(line)[1]

    LCD.LCD_ShowImage(image,50,50)

    


def screen_setup():
    LCD = LCD_1in44.LCD()

    print( "**********Init LCD**********")
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()
    
    
def random_chars() : 
    
    screen_setup()
    random.seed(1)

    while(True):
        s = 'abcdefghijklmnopqrstuvwxyzabcdefdfdfdfdfdfghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        new_s = [x for x in s]
        for (i,j) in enumerate(s):
            new_s[i] = s[random.randint(0,len(s)-1)] 
        main("".join(new_s))

if __name__ == '__main__':
    screen_setup()
    main(sys.argv[1])
