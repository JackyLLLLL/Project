import requests , json , time , os
from time import sleep
from datetime import datetime

#天氣小幫手
token = ""
response_status = 0
data = ""
weather_elements=""
set_time = '08:30'
prevent = True


def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

def get_data():
    global response_status , data,weather_elements
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-077"
    params = {
        "Authorization": "CWB-6CBC8455-EEB2-4458-80C2-F739B420DB75",
        "locationName":"七股區"
        #"limit": "1",
        #"offset": "30"
    }
    response = requests.get(url, params=params)
    response_status = response.status_code
    data = json.loads(response.text)
    weather_elements = data["records"]["locations"][0]["location"][0]["weatherElement"]

def weather_description():
    #天氣預報綜合描述
    item = 0
    weather_description = weather_elements[6]["description"]
    date = weather_elements[6]["time"][0]["startTime"]
    message = "\n%s\n日期%s" % (weather_description,date[0:10])
    #lineNotifyMessage(token, message)
    while item < 6:
        print(item)
        start_time = weather_elements[6]["time"][item]["startTime"]
        end_time = weather_elements[6]["time"][item]["endTime"]
        element_Value = weather_elements[6]["time"][item]["elementValue"][0]["value"]
        message = "\n七股區%s 時段:%s-%s\n綜合狀態:\n%s" %(weather_description,start_time[11:16],end_time[11:16],element_Value)
        print(message)
        item +=1
        #lineNotifyMessage(token, message)

def rain_prob():
    #降雨機率    
    item = 0
    description = weather_elements[7]["description"]
    date = weather_elements[7]["time"][0]["startTime"]
    print("%s\n日期%s" % (description,date[0:10]))
    while item < 2:
        start_time = weather_elements[7]["time"][item]["startTime"]
        end_time = weather_elements[7]["time"][item]["endTime"]
        rain_prob = weather_elements[7]["time"][item]["elementValue"][0]["value"]
        message = "時間:%s-%s 降雨機率:%s%%"%(start_time[11:16],end_time[11:16],rain_prob)
        print(message)
        item +=1
    print("")

def apparent_temp():
    #體感溫度
    item = 0
    apparent_temp = weather_elements[2]["description"]
    date = weather_elements[2]["time"][item]["dataTime"]
    print("%s\n日期%s" % (apparent_temp,date[0:10]))
    while item < 9:
        dataTime = weather_elements[2]["time"][item]["dataTime"]
        element_Value = weather_elements[2]["time"][item]["elementValue"][0]["value"]
        message = "時間:%s 溫度:%s度"%(dataTime[11:16],element_Value)
        print(message)
        item +=1
    print("")

get_data()
if response_status == 200:
    weather_description()
    #rain_prob()
    #apparent_temp()


while True:
    try:
        print('get times from file ok!')
        current_time = datetime.today().strftime("%H:%M")
        print('Time now it : '+current_time)
        if current_time == set_time and prevent == False:
            print('Run Weater Message Send !')
            get_data()
            if response_status == 200:
                weather_description()
        prevent = False

        time.sleep(60)
    except Exception as e:
        print(e)
