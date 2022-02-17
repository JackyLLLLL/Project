import pyautogui
import pyperclip
from time import sleep

screen_size = pyautogui.size()
user_msg = str(input("say something.. : "))

try:
    while True or a==0:
        start_botton = pyautogui.locateCenterOnScreen('start_chat.png',grayscale=True,confidence=0.95)
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
             sleep(1)
             pyautogui.click( start_botton)
             print('click start botton  successfully!')
             #pyautogui.MoveTo()
             pyautogui.moveTo(x=800,y=0)
             print('moving the mouse !')
             #sleep(5)
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
                    sleep(0.3)
                    pyautogui.press("Enter")
                    print("Press Enter")
                    a = 2
                    
                    while a ==2:
                         left_botton = pyautogui.locateCenterOnScreen('left_button.png',grayscale=True,confidence=0.9)
                         confirm_button = pyautogui.locateCenterOnScreen('confirm_button.png',grayscale=True,confidence=0.9)
                         start_botton = pyautogui.locateCenterOnScreen('start_chat.png',grayscale=True,confidence=0.9)
                         left_image = pyautogui.locateCenterOnScreen('left.png',grayscale=True,confidence=0.9)
                         
                         #print("a2 left_botton status: ",left_botton)
                         #print("a2 confirm_button status: ", confirm_button)
                         #print("a2 start_botton status: ",  start_botton)
                         #print("a2 left_image status: ",  left_image)
                         #sleep(1)
                         
                         if left_image is not None:
                              pyautogui.click(left_botton)
                              print('click left_botton successfully!')
                              a = 0
                         elif confirm_button  is not None:
                             pyautogui.click(confirm_button)
                             print('click confirm_button successfully!')
                             a = 0
                         else:
                              print('Failed to find left button !')
                        
                 else:
                    print('Failed to find messanger!')
                
        else:
            print('Failed to find start botton!')

        
except KeyboardInterrupt:
    print("Close Program")
        
##width, height = pyautogui.size()

##print(width,height)
##
##pyautogui.typewrite('Hello')

##pyperclip.copy("你好")
##pyautogui.hotkey("ctrl","v")

##while True:
##    x,y = pyautogui.position()
##    print(str(x),str(y))
    
