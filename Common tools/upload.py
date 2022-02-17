import paramiko
import os
import datetime
import time


hostname=''
username=''
password=''
port=22

def upload(local_dir,remote_dir):
    try:
        t=paramiko.Transport((hostname,port))
        t.connect(username=username,password=password)
        sftp=paramiko.SFTPClient.from_transport(t)
        print ('upload file start %s' % datetime.datetime.now())

        for root,dirs,files in os.walk(local_dir):
            
            for filespath in files:
                local_file = os.path.join(root,filespath)
                a = local_file.replace(local_dir,'')
                remote_file = os.path.join(remote_dir,a)
                
                try:
                    sftp.put(local_file,remote_file)
                except Exception as e:
                    sftp.mkdir(os.path.split(remote_file)[0])
                    sftp.put(local_file,remote_file)
                print ("upload %s to remote %s" % (local_file,remote_file))

            for name in dirs:
                local_path = os.path.join(root,name)
                a = local_path.replace(local_dir,'')
                remote_path = os.path.join(remote_dir,a)
                
                try:
                    sftp.mkdir(remote_path)
                    print ("mkdir path %s" % remote_path)
                except Exception as e:
                    print (e)
        
        print ('upload file success %s ' % datetime.datetime.now())
        t.close()

    except Exception as e:
        print (e)

t = time.localtime()
ymd = time.strftime("%Y.%m.%d",t)



if __name__=='__main__':

    local_dir='/home/pi/Ultrasonic/sonar_result_data/%s/'%ymd
    remote_dir='/home/ubuntu/disk2/sonar_result_data/%s/'%ymd
    upload(local_dir,remote_dir)

