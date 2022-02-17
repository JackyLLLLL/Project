#-*- coding: utf-8 -*- 
#!/usr/bin/python

import paramiko #導入paramiko模組
import threading #導入threading模組

def sftp(ip,username,passwd,remotepath):  #這裡定義一個函式命名為sftp
    
    try:
        tran = paramiko.Transport(ip,port) #建立Transport物件
        tran.connect(username = username, password = passwd)#連線SSH服務端
        sftp = paramiko.SFTPClient.from_transport(tran)     #獲取SFTP例項
        localpath=r'C:\Users\user\Desktop\File_transfer_Test.txt' ##設定本地檔案路徑存到變數localpath裡
        sftp.put(localpath,remotepath)  #執行上傳動作
        print('File Successfully transmitted...')
        print ('%s\tOK\n'%(ip))
        print('============')
        tran.close() #關閉連線
        
    except : 
        print ('%s\tError\n'%(ip))  #若程式異常則執行這邊

if  __name__=='__main__' :
    #__name__ 是當前模組名，當模塊被直接運行時模組名為 __main__ 。
    #這句話的意思就是，當模組被直接運行時，以下代碼塊組被運行，當模組是被導入時，代碼則不被運行。

    #username = 'user' 
    passwd = '' #將使用者密碼存到passwd變數裡面
    port = 22  #通訊埠使用22，一般port22用於安全檔案傳輸(SSH、SCP、SFTP)
    remotepath1=r"C:\Users\User\Desktop\File_transfer_Test.txt" #第一台目標主機要上傳檔案的遠端儲存路徑存到變數
    remotepath2=r"C:\Users\MyUser\Desktop\File_transfer_Test.txt" #第二台目標主機要上傳檔案的遠端儲存路徑存到變數
    threads = []  #多執行緒


info =[
      ('10.192.172.115','user',passwd,remotepath1),
      ('10.192.183.122','myuser',passwd,remotepath2)
      ]

#將(ip_address,username,passwd,remotepath)使用tuple的方式儲存起來
#再將Tuple使用List存放

for info in info: #使用For迴圈遍歷list內所有ip位址
    a=threading.Thread(target=sftp,args=info)
    a.start()
    #使用多執行緒同時執行

# 注意：
# 該輸入的都有輸出，但有些順序搶先輸出了，這也代表不同核心接到任務的順序。
# 所以「每次執行不一定相同」






