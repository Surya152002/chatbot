import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller,Button
from time import sleep
#mouse clicking
mouse=Controller()
#Instruction for Whatsapp Bot
class Whatsapp:
    #Defines the starting value
    def __int__(self,speed=.5,click_speed=.3):
        self.speed =speed
        self.click_speed=click_speed
        self.message=''
        self.last_message=''
    #Navigate to the green dots for new message
    def nav_green_dot(self):
        try:
            position=pt.locateOnScreen('green_dot.png',confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(-100,0,duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot): ',e)
wa_bot = Whatsapp(speed=.5,click_speed=.4)
sleep(2)
wa_bot.nav_green_dot()