import serial
import time
from time import sleep
import random

s_obj = serial.Serial('/dev/ttyUSB0', baudrate=115200, 
        bytesize=8, parity='N', stopbits=1, timeout=1)

#s_obj = serial.Serial("COM6", baudrate=115200, 
#        bytesize=8, parity='N', stopbits=1, timeout=2)

text = "Hello World"

try:
    while True:

        random_num = (random.uniform(1,100))
        send_mes = str("%.2f"%random_num)
        t = time.localtime()
        clock = time.strftime("%H:%M:%S",t)
        write = s_obj.write(send_mes.encode())
        print(f'Transmit: {send_mes},',clock) 
        #print(f'{text},',clock)
        sleep(1)
except KeyboardInterrupt:
    print("Close the program")

except Exception as e:
    print(e)

finally:
    s_obj.close()
