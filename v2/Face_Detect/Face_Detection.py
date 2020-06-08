from flask import Flask,request
import requests as re
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random
import time
import json

app = Flask(__name__)


headers = {'Content-Type':'application/json'}
def Push_Data(data):


    #prometheus gateway metric
	registry = CollectorRegistry()
 
	g = Gauge('Face_Dection_Time','Face_Detection processing time',registry=registry)

	g.set(data)

	push_to_gateway('http://192.168.2.1:9092',job='Face_Dectector',registry=registry)

def Face_Detect():
	time = random.randint(30,120)
	
	
	return time


_url = "http://"
headers = {'Content-Type':'application/json'}
@app.route("/",methods=['POST','GET'])
def main():
	pass
	flag = 0
	
	if request:
		
		url = _url + "face-feature-extractor:5000"
		
		data = request.get_json(silent=True)
		
		data['detect_time'] = Face_Detect()

		re.post(url,headers=headers,data=json.dumps(data))

		Push_Data(data['detect_time'])

		
		return "OK"
		

	


if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000,threaded=True)
