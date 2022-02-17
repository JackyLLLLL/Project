import pyautogui
import pyperclip
from time import sleep

# Test catch image status

"""
while True:
    start = pyautogui.locateCenterOnScreen('start.png',grayscale=True,confidence=0.9)
    mess = pyautogui.locateCenterOnScreen('mess.png',grayscale=True,confidence=0.9)
    restart = pyautogui.locateCenterOnScreen('restart.png',grayscale=True,confidence=0.9)
    print("----------")
    print("start status:",start)
    print("mess status: ",mess)
    print("restart status: ",restart)
    print("----------")
    sleep(1)
"""

def click_start():
    while True:
        sleep(1)
        start = pyautogui.locateCenterOnScreen('start.png',grayscale=True,confidence=0.9)
        print("--------------------")
        print("start status:",start)
        if  start is not None:
             pyautogui.click(start)
             print('Opened start menu successfully!')
             return "start_function was used"
        else:
            print('Failed to open start menu!')
     
       
def messanger():
    while True:
        sleep(1)
        mess = pyautogui.locateCenterOnScreen('mess.png',grayscale=True,confidence=0.9)
        print("--------------------")
        print("mess status: ",mess)
        if mess is not None:
            pyautogui.click(mess)
            print("click the message box")
            pyperclip.copy("test the program")
            pyautogui.hotkey("ctrl","v")
            print("Paste text")
            pyautogui.press("Enter")
            print("Press Enter")
            return "mess_function was used"
        else:
            print('Failed to find messanger!')
  
def click_restart():
    while True:
        sleep(1)
        restart = pyautogui.locateCenterOnScreen('restart.png',grayscale=True,confidence=0.9)
        print("--------------------")
        print("restart status: ",restart)
        if restart is not None:
            pyautogui.click(restart)
            print('click restart button successfully!')
            return "restart_function was used"
        else:
            print('Failed to find restart button!')

while True:
    start = click_start()
    if start == "start_function was used" :
        mes = messanger()
       
        if mes == "mess_function was used" :
            restart = click_restart()
        
                
            

             


        
    
    
    
    

