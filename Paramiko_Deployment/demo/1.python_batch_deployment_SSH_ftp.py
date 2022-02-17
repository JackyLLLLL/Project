#-*- coding: utf-8 -*- 
#!/usr/bin/python

import paramiko #導入paramiko模組
import threading #導入threading模組

def sftp(ip,username,passwd,remotepath):  #這裡定義一個函式命名為sftp
    
    try:
        tran = paramiko.Transport(ip,port) #獲取Transport例項 
        tran.connect(username = username, password = passwd)#連線SSH服務端
        sftp = paramiko.SFTPClient.from_transport(tran)     #獲取SFTP例項
        localpath=r'C:\Users\user\Desktop\Logs_20220117.txt' ##設定本地檔案路徑存到變數
        sftp.put(localpath,remotepath)  #執行上傳動作
        print('File Successfully transmitted...')
        print ('%s\tOK\n'%(ip))
        print('============')
        tran.close() #關閉連線
        
    except : 
        print ('%s\tError\n'%(ip))  #異常則執行這邊

if  __name__=='__main__' :
    username = '' 
    passwd = '' #將使用者密碼存到passwd變數裡面
    port = 22  #通訊埠使用22，一般port22用於安全檔案傳輸(SSH、SCP、SFTP)
    remotepath="/home/pi/Logs_20220117.txt" ##設定要上傳檔案的遠端儲存路徑
    
    threads = []  #多執行緒


ip = (
        '10.192.172.148',
        '10.192.172.249',
         )

#將要遠端ip位址存到Tuple裡面

for ip in ip: #使用For迴圈遍歷Tuple內所有ip位址
    a=threading.Thread(target=sftp,args=(ip,username,passwd,remotepath))
    a.start()
    #使用多執行緒同時執行







##if __name__=='__main__':
##  username = "pi" #使用者名稱
##  port = 22
##  passwd = ""  #密碼 
##  threads = []  #多執行緒 
##  print ("Begin......")
##  
##ip = ('10.192.172.120','10.192.172.116')
##
##for ip in ip:
##    a=threading.Thread(target=sftp,args=(ip,port,username,passwd))
##    a.start()

