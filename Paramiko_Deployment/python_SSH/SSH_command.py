#-*- coding: utf-8 -*- 
#!/usr/bin/python  
import paramiko 
import threading 
def ssh2(ip,username,passwd,cmd): 
  try: 
    ssh = paramiko.SSHClient() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    ssh.connect(ip,22,username,passwd,timeout=5) 
    for m in cmd: 
      stdin, stdout, stderr = ssh.exec_command(m) 
#      stdin.write("Y")  #簡單互動，輸入 ‘Y'
      for o in stdout:
            #out = stdout.readlines() 
            #螢幕輸出 
            #for o in out: 
        print (o) 
    print ('%s\tOK\n'%(ip))
    print('============')
    ssh.close() 
  except : 
    print ('%s\tError\n'%(ip))
    
if __name__=='__main__': 
  #cmd = ['cd /home/pi/Jacky;pwd;ls']#你要執行的命令列表
  cmd = ['cd /home/pi/pi_auto/udp ; pwd ;tar zxvf send_udp.tar.gz ; sudo chmod 644 udp_client.py ; sudo systemctl restart udp_client.service ; systemctl status udp_client.service']
  #cmd = ['systemctl status udp_client.service']
  username = "" #使用者名稱 
  passwd = ""  #密碼 

  print ("Begin......")

ip = ('10.192.172.120', '10.192.172.116')

for ip in ip:
    a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
    a.start()



##  for i in range(116,121): 
##    ip = '10.192.172.'+str(i) 
##    a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))  
##    a.start() 
