#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko

address_ip ="0.0.0.0"
username ="user"
pwd ="password"

##1.建立一個ssh物件 
client = paramiko.SSHClient() 
#2.解決問題:如果之前沒有，連線過的ip，會出現選擇yes或者no的操作， 
##自動選擇yes 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
#3.連線伺服器 
client.connect(hostname=address_ip, 
 port=22, 
 username=username, 
 password=pwd) 
#4.執行操作 
stdin,stdout, stderr = client.exec_command('hostname;dir') 
#5.獲取命令執行的結果
#result=stdout.read().strip()
result=stdout.read().decode('Big5')

print (result)
#6.關閉連線 
client.close() 
