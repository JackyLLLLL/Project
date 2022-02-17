import pyautogui
import pyperclip
from time import sleep

start = pyautogui.locateCenterOnScreen('start.png',grayscale=True,confidence=0.9)
mess = pyautogui.locateCenterOnScreen('mess.png',grayscale=True,confidence=0.9)
restart = pyautogui.locateCenterOnScreen('restart.png',grayscale=True,confidence=0.9)


#while True:
#   mouse = pyautogui.position()
#   print(mouse)
#   sleep(1)

print("點擊Crtl + C 關閉程式")

count = 0
while True:
    start = pyautogui.locateCenterOnScreen('start.png',grayscale=True,confidence=0.9)
    mess = pyautogui.locateCenterOnScreen('mess.png',grayscale=True,confidence=0.9)
    restart = pyautogui.locateCenterOnScreen('restart.png',grayscale=True,confidence=0.9)
    
    while count == 0 :
        if start is not None:
            pyautogui.click(start)
            print("已捕捉到Start Photo")
            print("loading..")
            sleep(5)
            count = 1
        else:
            print("沒有捕捉到Start Photo")
            sleep(1)

    while count == 1 :
        if mess != None:
            pyautogui.click(mess)
            print("已捕捉到mess photo")
            pyperclip.copy("Hello")
            print("copy文字")
            pyautogui.hotkey("ctrl","v")
            print("貼上文字")
            pyautogui.press("Enter")
            print("按Enter")
            sleep(5)
            count = 2
        else:
            print("沒有抓到對話框的圖片")
            sleep(1)

    while count == 2:
        if restart != None:
            pyautogui.click(restart)
            print("已捕捉到restart Photo")

        else:
            count = 0
            print("回到開始")    

