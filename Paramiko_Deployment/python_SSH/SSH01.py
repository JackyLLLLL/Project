import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("0.0.0.0",22,"user", "password")
stdin, stdout, stderr = ssh.exec_command("dir")
for x in stdout:
    print (x,end="")
ssh.close()
