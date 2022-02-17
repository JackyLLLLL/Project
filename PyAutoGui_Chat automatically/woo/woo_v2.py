import pyautogui
import pyperclip
from time import sleep

screen_size = pyautogui.size()
user_msg = str(input("say something.. : "))

try:
    while True or a==0:
        start_botton = pyautogui.locateCenterOnScreen('start_chat.png',grayscale=True,confidence=0.97)
        message_box = pyautogui.locateCenterOnScreen('woo_messange_box.png',grayscale=True,confidence=0.9)
        left_botton = pyautogui.locateCenterOnScreen('left_button.png',grayscale=True,confidence=0.9)
        confirm_button = pyautogui.locateCenterOnScreen('confirm_button.png',grayscale=True,confidence=0.9)
        left_image = pyautogui.locateCenterOnScreen('left.png',grayscale=True,confidence=0.8)

        
##        print("----------")
##        print("start_botton status:", start_botton)
##        print("message_box status: ",message_box)
##        print("left_botton status: ",left_botton)
##        print("confirm_button status: ", confirm_button)
##        print("left_image status: ",left_image)
##        print("----------")
        
        
        if   start_botton is not None:
             pyautogui.click(start_botton)
             print('click start botton  successfully!')
             pyautogui.moveTo(x=1500,y=450)
             print('moving the mouse !')
             a=1
             
             while a == 1:
                 message_box = pyautogui.locateCenterOnScreen('woo_messange_box.png',grayscale=True,confidence=0.9)
                 print("a1 mess status: ",message_box)
                 sleep(1)
                     
                 if message_box is not None:
                    pyautogui.click(message_box)
                    print("click the message box")
                    pyperclip.copy(user_msg)
                    pyautogui.hotkey("ctrl","v")
                    print("Paste text")
                    sleep(0.6)
                    pyautogui.press("Enter")
                    print("Press Enter")
                    break
                
                 else:
                   print('Failed to find messanger!')
                   
        elif left_image is not None:
              pyautogui.click(left_botton)
              print('click left_botton successfully!')
              a = 0
        elif confirm_button  is not None:
              pyautogui.click(confirm_button)
              sleep(0.2)
              print('click confirm_button successfully!')
              pyautogui.moveTo(x=1500,y=450)
              sleep(0.5)
              a = 0
        else:
            print('Failed to find start botton!')

 

        
except KeyboardInterrupt:
    print("Close Program")

