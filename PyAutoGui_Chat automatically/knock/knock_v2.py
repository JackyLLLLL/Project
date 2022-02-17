import pyautogui
import pyperclip
from time import sleep


screen_size = pyautogui.size()
user_msg = str(input("say something.. : "))

try:
    while True or a==0:
        start = pyautogui.locateCenterOnScreen('start.png',grayscale=True,confidence=0.9)
        mess = pyautogui.locateCenterOnScreen('mess.png',grayscale=True,confidence=0.9)
        restart = pyautogui.locateCenterOnScreen('restart.png',grayscale=True,confidence=0.9)
##        print("----------")
##        print("start status:",start)
##        print("mess status: ",mess)
##        print("restart status: ",restart)
##        print("----------")
        
        if  start is not None:
             pyautogui.click(start)
             print('click start botton successfully!')
             sleep(5)
             a=1

             while  a == 1:
                 mess = pyautogui.locateCenterOnScreen('mess.png',grayscale=True,confidence=0.9)
                 print("a1 mess status: ",mess)
                 sleep(1)

                 if mess is not None:
                    pyautogui.click(mess)
                    print("click the message box")
                    pyperclip.copy(user_msg)
                    pyautogui.hotkey("ctrl","v")
                    print("Paste text")
                    pyautogui.press("Enter")
                    print("Press Enter")
                    break

                 else:
                   print('Failed to find messanger!')
             
        elif restart is not None:
             pyautogui.click(restart)
             print("Restart status: ",restart)
             sleep(2)
             a=1
             
             while  a == 1:
                mess = pyautogui.locateCenterOnScreen('mess.png',grayscale=True,confidence=0.9)
                print("a1 mess status: ",mess)
                sleep(1)

                if mess is not None:
                    pyautogui.click(mess)
                    print("click the message box")
                    pyperclip.copy(user_msg)
                    pyautogui.hotkey("ctrl","v")
                    print("Paste text")
                    pyautogui.press("Enter")
                    print("Press Enter")
                    break

                else:
                   print('Failed to find messanger!')

        else:
            print('Failed to find start or restart botton !')

        
except KeyboardInterrupt:
    print("Close Program")

