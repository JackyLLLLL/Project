import pyautogui
import pyperclip
from time import sleep


screen_size = pyautogui.size()

##while True:
##    start = pyautogui.locateCenterOnScreen('start.png',grayscale=True,confidence=0.9)
##    mess = pyautogui.locateCenterOnScreen('mess.png',grayscale=True,confidence=0.9)
##    restart = pyautogui.locateCenterOnScreen('restart.png',grayscale=True,confidence=0.9)
##    print("----------")
##    print("start status:",start)
##    print("mess status: ",mess)
##    print("restart status: ",restart)
##    print("----------")
##    sleep(1)

def click_start():
    while True:
        sleep(1)
        start = pyautogui.locateCenterOnScreen('start.png',grayscale=True,confidence=0.9)
        print("--------------------")
        print("start status:",start)
      
        if  start is not None:
             pyautogui.click(start)
             print('Opened start menu successfully!')
        else:
            print('Failed to open start menu!')
  
def messanger():
    while True:
        sleep(1)
        mess = pyautogui.locateCenterOnScreen('mess.png',grayscale=True,confidence=0.9)
        
        if mess is not None:
            pyautogui.click(mess)
            print("點擊對話框")
            pyperclip.copy("Hello")
            pyautogui.hotkey("ctrl","v")
            print("貼上文字")
            pyautogui.press("Enter")
            print("按Enter")
        else:
            print('Failed to find messanger!')
 
def click_restart():
    while True:
        sleep(1)
        restart = pyautogui.locateCenterOnScreen('restart.png',grayscale=True,confidence=0.9)
        if restart is not None:
            pyautogui.click(restart)
            print('click restart button successfully!')
        else:
            print('Failed to find restart button!')
       
while True:
    click_start()
