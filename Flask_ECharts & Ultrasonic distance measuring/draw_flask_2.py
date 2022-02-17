import json
import time
from datetime import datetime
from flask import Flask, Response, render_template
import pandas as pd #讀檔

data = "/home/pi/Flask_Demo/for_demo.csv"

df = pd.read_csv(data,encoding= 'big5')
# y_change1 = df["Sensor1"].values.tolist()
ddd = df["Date"].values.tolist() #日期
# now =  df["Time"].values.tolist() #幾點幾分



application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html',ddd=ddd[-1])

@application.route('/chart-data')

def chart_data():
    def generate_random_data():   
        while True:
            
            df = pd.read_csv(data,encoding= 'big5')
            y_change1 = df["Sensor2"].values.tolist()
            now =  df["Time"].values.tolist() #幾點幾分
            
            json_data = json.dumps(
                {'time':now[-1], 'value': y_change1[-1]})
            yield f"data:{json_data}\n\n"           

            time.sleep(1)

                
    return Response(generate_random_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    application.run(host='10.192.172.111',port='5000',debug=True, threaded=True)
    

#後續目標
#即時更新數據
#拉動時間軸
#指定時間開始跑資料
#重啟網頁時不會重跑資料
