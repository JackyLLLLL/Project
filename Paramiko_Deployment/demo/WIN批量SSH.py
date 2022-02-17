#-*- coding: utf-8 -*- 
#!/usr/bin/python

import paramiko #導入paramiko模組
import threading #導入threading模組

def ssh2(ip,username,passwd,cmd):  #這裡定義一個函式命名為ssh2
  try: 
    ssh = paramiko.SSHClient() #建立ssh物件
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 允許連線不在know_hosts檔案中的主機
    ssh.connect(ip,22,username,passwd,timeout=5) #連線遠端
    for m in cmd: #使用For迴圈遍歷list內所有命令
      stdin, stdout, stderr = ssh.exec_command(m)
      out = stdout.read().decode('Big5') #讀取獲取命令結果並且用Big5解碼 
      print (out)  #輸出獲取命令的結果
      
    print ('%s\tOK\n'%(ip))
    print('============')
    ssh.close()  #關閉連線
    
  except : 
    print ('%s\tError\n'%(ip)) #若程式異常則執行這邊
    
if __name__=='__main__': 
#__name__ 是當前模組名，當模塊被直接運行時模組名為 __main__ 。
#這句話的意思就是，當模組被直接運行時，以下代碼塊組被運行，當模組是被導入時，代碼則不被運行。

  cmd = ['ipconfig','hostname','dir'] #把要執行的命令使用List方式存到cmd變數裡
  #username = "user" #使用者名稱 
  passwd = ""  #密碼 
  threads = []  #多執行緒
  print ("Begin......")

info =[
      ('10.192.172.115','user',passwd,cmd),
      ('10.192.183.122','myuser',passwd,cmd)
      ]
#將(ip_address,username,passwd,remotepath)使用tuple的方式儲存起來
#再將Tuple使用List存放

for info in info: #使用For迴圈遍歷list內所有ip位址
  a=threading.Thread(target=ssh2,args=info)
  a.start()
  #使用多執行緒同時執行

#a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))

# 注意：
# 該輸入的都有輸出，但有些順序搶先輸出了，這也代表不同核心接到任務的順序。
# 所以「每次執行不一定相同」




