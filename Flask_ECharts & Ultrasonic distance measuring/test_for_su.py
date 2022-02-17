from smbus import SMBus
from time import sleep
from datetime import datetime
import os
import time
import csv

i2cbus1 = SMBus(3)

def sensor_2_distance():
    try:
        i2cbus1.write_byte(0x70, 0x51) 
        val1 = i2cbus1.read_word_data(0x70, 0xe1)
        detector_2_distance = (val1 >> 8) & 0xff | (val1 & 0xff) << 8
        return detector_2_distance
    except IOError:
        detector_2_distance = 0
        return detector_2_distance 

sensor_end_time =  datetime.now().timestamp()
sensor_final_keep_time = 0

def sensor_2_keep_time():
    global sensor_end_time
    global sensor_final_keep_time

    sensor_start_time = keep_time = 0
    detector_2_distance = int(sensor_2_distance())
    
    if detector_2_distance < 50:
        sensor_start_time = datetime.now().timestamp()  
        keep_time = sensor_start_time - sensor_end_time
        sensor_final_keep_time = round(keep_time,2)
    
    if detector_2_distance > 50:
        sensor_end_time = datetime.now().timestamp()
        keep_time = 0 
        
    keep_time = round(keep_time,2)
    return keep_time 
    #return sensor_final_keep_time
    keep_time = 0


item = 1
start_time = "08:00"
end_time = "17:00"
prevent = True


try:
    while True:
        
        detector_2_distance = str(sensor_2_distance())
        detector_2_keep_time = sensor_2_keep_time()
        
        t = time.localtime()
        
        ymd   = time.strftime("%Y.%m.%d",t)
        date  = time.strftime("%Y%m%d",t)
        hour  = time.strftime("%H",t)
        current_time = str(time.strftime("%H:%M",t))
        sec_time = datetime.now().strftime('%H:%M:%S:%f')[:-4]
        
        title = ["Item","Sensor2","KeepTime","Date","Time"] 
        table = [item,detector_2_distance,detector_2_keep_time,ymd,sec_time]
        
        dir_path = "/home/pi/Ultrasonic/sonar2_result_data/"
        data_dir_path = "/home/pi/Ultrasonic/sonar2_result_data/%s/"%ymd
        #data_file_name = data_dir_path+"Sonar2Data"+str(date)+"_"+str(hour)+'.csv'
        data_file_name = "/home/pi/Flask_Demo/for_demo.csv"
        
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
            
        if not os.path.isdir(data_dir_path):
            os.mkdir(data_dir_path)
         
        if current_time >= start_time and current_time <= end_time and prevent == False:
            if not os.path.isfile(data_file_name):

                with open(data_file_name,'w') as csvfile:
                    writer =csv.writer(csvfile)
                    writer.writerow(title)

            with open(data_file_name,'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(table)
            
        print(table)

        prevent = False 
            
        item +=1
        sleep(0.1)



except  KeyboardInterrupt: 
    print('Close the Program')


except Exception as e:
    print(e)
    sleep(1)


