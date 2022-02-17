import serial
import time
from time import sleep


s_obj = serial.Serial('/dev/ttyUSB0', baudrate=115200, 
        bytesize=8, parity='N', stopbits=1, timeout=2)

try:
    while True:

        t = time.localtime()
        clock = time.strftime("%H:%M:%S",t)
        
        data = s_obj.read(s_obj.inWaiting()) 
        
        if data != b'' :
            recv_data=data.decode('utf-8','replace')
            print(f'Recv: {recv_data} ,{clock}')

        elif data == b'' or not data:
            print('No data received,',clock)
        else:
            print('Program Error,',clock)
        sleep(1)

except KeyboardInterrupt:
    print("Close the program")

except Exception as e:
    print(e)

finally:
    s_obj.close()

