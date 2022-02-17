#匯入模組
import random
import tkinter as tk
import tkinter.messagebox as tmsg #匯入messagebox 套件


# 當按鈕被點擊時的處理
def ButtonClick():
    # 取得文字輸入欄位裡的輸入字串
    b=editbox1.get()


    # Lesson 5-4 的程式
    # 判斷是否為4位數字
    isok = False
    if len(b) != 4:
        tmsg.showerror("錯誤","請輸入4位數的數字: ")
    else:
        kazuok = True
        for i in range(4):
            if (b[i] <"0") or (b[i] > "9") :
                tmsg.showerror("錯誤","並非數字")
                kazuok = False
                break
        if kazuok :
            isok = True
    if isok:
        # 當輸入4位數的數字時
        # 判斷 hit
        hit = 0
        for i in range(4):
            if a[i] == int(b[i]):
                hit = hit + 1

    #  判斷Blow
    blow = 0
    for j in range(4):
      for i in range(4):
        if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
          blow = blow + 1
          break
    # 當 hit 為4時結束
    if hit == 4:
        tmsg.showinfo("猜中了","恭喜恭喜 ! 猜中了")
    # 結束
        root.destroy()
    else:
        #顯示Hit數量與Blow數量
        rirekibox.insert(tk.END,b+" A: "+str(hit)+"B: "+str(blow)+"\n")
        tmsg.showinfo("提示","Hit"+str(hit)+"/"+"Blow"+str(blow))

#主要的程式
#先準備好一開始的4個隨機數字
a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]

# 製作視窗
root = tk.Tk()
root.geometry("600x400")
root.title("猜數字遊戲")
#製作顯示紀錄的文字方塊
rirekibox=tk.Text(root,font=("Helvetica",14))
rirekibox.place(x=400,y=0, width=200,height=400)
#製作標籤
label1 = tk.Label(root, text="請輸入數字喔: ", font=("Helvetica", 14))
label1.place(x = 20, y = 20)
#製作文字方塊
editbox1 = tk.Entry(width = 4, font=("Helvetica", 28))
editbox1.place(x = 120, y = 60)
#製作按鈕
button1 = tk.Button(root, text = "確認", font=("Helvetica", 14),command=ButtonClick)
button1.place(x = 220, y = 60)
#顯示視窗
root.mainloop()
