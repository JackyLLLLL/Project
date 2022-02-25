import requests
import json

def get_data():
    

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
        weather_state = data["records"]["locations"][0]["location"][0]["weatherElement"][6]["time"]
    
        for weather_state in weather_state:
            
            startTime = weather_state["startTime"]
            endTime = weather_state["endTime"]
            elementValue = weather_state["elementValue"]
            value = elementValue[0]["value"]
                 
            print(type(startTime))
        
          
  

        
     
      
        
        #startTime =  weather_state["startTime"]
        #endTime =
        #elementValue =
        #print (type(weather_state))
        #print (weather_state)
        #print( startTime)
      
       # print(startTime)
        

        
##        weather_elements = data["records"]["locations"][0]["location"][0]["weatherElement"] #天氣狀態
##        start_time = weather_elements[0]["time"][0]["startTime"] 
##        end_time = weather_elements[0]["time"][0]["endTime"]        
##        weather_state = weather_elements[0]["time"][2]["elementValue"][0]
        
##        rain_prob = weather_elements[1]["time"][0]["parameter"]["parameterName"]
##        min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
##        comfort = weather_elements[3]["time"][0]["parameter"]["parameterName"]
##        max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]
##
##        print(location)    
##        print(weather_elements)       
##        print(start_time)
##        print(weather_state)
##        print(end_time)       
##        print(rain_prob)
##        print(min_tem)
##        print(comfort)
##        print(max_tem)

    else:
        print("Can't get data!")
        
def line_notify():

    api = "CWB-3E23CE1A-37CB-4F82-8931-D3D85797A941"
    token ="QJUoBshGivcJs2cfhcopkuXhdJf6F177tLHF8hdeqFy"
    message = "Hello! 測試一下串接LINE的API!"
   

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


if __name__ == '__main__':
    get_data()
    #line_notify()
