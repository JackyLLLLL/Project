import requests
import json
import time
from datetime import datetime
from time import sleep

def get_data(i):
    global result

    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-077"


    params = {
        "Authorization": "CWB-3E23CE1A-37CB-4F82-8931-D3D85797A941",
        "locationName": "安南區",
    }

    response = requests.get(url, params=params)
    print(response.status_code) #API連線狀況

    if response.status_code == 200:
        #print(response.text)
        data = json.loads(response.text)
  
       
        location = data["records"]["locations"][0]["location"][0]["locationName"] #地區
        weather_status = data["records"]["locations"][0]["location"][0]["weatherElement"][6]["time"]        
        
        weather_state = weather_status[i]
          
        dateTime = weather_state["startTime"][0:11]
        startTime = weather_state["startTime"][11:-3]
        endTime = weather_state["endTime"][11:16]
        elementValue = weather_state["elementValue"]
        value = elementValue[0]["value"]
        value = value.split("。")
        weather_state = value[0]
        rain_prob = value[1][-3:]
        temp = value[2][4:-1]
        comfort =value[3]
        wind = value[4]
        humidy = value[5]
       
        result = (f"\n日期:{dateTime}\n時間:{startTime}~{endTime}\n狀態:{weather_state}\n降雨機率:{rain_prob}\n目前溫度:{temp}°C\n體感:{comfort}\n風向:{wind}\n{humidy}")
        print(result)
                 
     
    else:
        print("Can't get data!")
        
def line_notify():

    api = "CWB-3E23CE1A-37CB-4F82-8931-D3D85797A941"
    token ="QJUoBshGivcJs2cfhcopkuXhdJf6F177tLHF8hdeqFy"
    message = result
    #message = result
   

    # line notify所需資料
    line_url = "https://notify-api.line.me/api/notify"
    line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    line_data = {
        "message": message
    }

    requests.post(url=line_url, headers=line_header, data=line_data)


prevent = True

if __name__ == '__main__':

    while True:

        t = time.localtime()
        current_time = str(time.strftime("%H:%M",t))

   
        for i in range(24):
        
            if current_time == "06:00" and prevent == True :
                get_data(0)
                line_notify()
                prevent = False
                break
            if current_time == "09:00" and prevent == False :
                get_data(1)
                line_notify()
                prevent = True
                break
            if current_time == "12:00" and prevent == True :
                get_data(0)
                line_notify()
                prevent = False
                break
            if current_time == "15:00" and prevent == False :
                get_data(1)
                line_notify()
                prevent = True
                break
            if current_time == "18:00" and prevent == True :
                get_data(2)
                line_notify()
                prevent = False
                break
            if current_time == "21:00" and prevent == False :
                get_data(3)
                line_notify()
                prevent = True
                break
            
        print(f"目前時間是:{current_time},prevent={prevent}")
           
        sleep(50)
               
        
    #line_notify()
