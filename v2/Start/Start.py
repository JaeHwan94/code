from flask import Flask,render_template,request
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random
import requests as re
import json
from datetime import datetime as dt

app = Flask(__name__,template_folder='templates')

_url = "http://"
headers = {'Content-Type':'application/json'}

def Strat_Time():
	now = dt.now()

	time = {'month':now.month,'day':now.day,'hour':now.hour,'min':now.minute,'sec':now.second}
	
	data = "{}m-{}d-{}h-{}m-{}s".format(time['month'],time['day'],time['hour'],time['min'],time['sec'])

	return data,time

def Push_Data(data,time):


	#prometheus gateway metric
	registry = CollectorRegistry()

	g = Gauge('Process_Start_Time','Process start time',['start_time'],registry=registry)
	

	g.labels(start_time=data).set(time['min'])
	
	push_to_gateway('http://192.168.2.1:9092',job='Check_Start_Time',registry=registry)

@app.route("/start",methods=['GET','POST'])
def main():
	data = {}
	global _url

	
	if request:
		port = ":5000"
			
		url = _url+'face-detection'+port

		data['start_time'],time = Strat_Time()

		re.post(url,headers=headers,data=json.dumps(data))
		
		Push_Data(data['start_time'],time)
			

		return "OK" 
	


if __name__ == "__main__":
	 

	app.run(host="0.0.0.0",port=5000, threaded=True)



