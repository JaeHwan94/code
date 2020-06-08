from flask import Flask,request
import requests as re
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random
import time
import json

app = Flask(__name__)

def Push_Data(data):

    #prometheus gateway metric
	registry = CollectorRegistry()
	g = Gauge('Face_Feature_Extract_Time','Face_Feature_Extract processing time',registry=registry)
	g.set(data)
	push_to_gateway('http://192.168.2.1:9092',job='Face_Feature_Extractor',registry=registry)



def Face_Extract():
	time = random.randint(30,120)
	
	
	return time


_url = "http://"
headers = {'Content-Type':'application/json'}

@app.route("/",methods=['POST','GET'])
def main():
	global _url
	if request:
		group = {"A":"membera:5000","B":"memberb:5000"}
		
		data = request.get_json(silent=True)

		data['extract_time'] = Face_Extract()

		
		url = _url+group['A']
		re.post(url,headers=headers,data=json.dumps(data))
		
		url = _url+group['B']
		re.post(url,headers=headers,data=json.dumps(data))
		

		Push_Data(data['extract_time'])

		return "OK"
		
		

	


if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000,threaded=True)
