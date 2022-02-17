#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko

address_ip ="0.0.0.0"  
username ="user"
pwd =""

##1.建立一個ssh物件 
client = paramiko.SSHClient() 
#2.解決問題:如果之前沒有，連線過的ip，會出現選擇yes或者no的操作， 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) ##自動選擇yes 
#3.連線伺服器 
client.connect(hostname=address_ip, 
port=22, 
username=username, 
password=pwd) 
#4.執行操作 
stdin,stdout, stderr = client.exec_command('hostname;cd Desktop;dir') 
#5.獲取命令執行的結果
result=stdout.read().decode('Big5')
print (result) #輸出結果
#6.關閉連線 
client.close()


##############
#windows Big 5
#linux utf-8
