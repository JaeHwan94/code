from flask import Flask,request
import requests as re
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random
import time
import json

app = Flask(__name__)


headers = {'Content-Type':'application/json'}

def Face_Detect():
	time = random.randint(30,120)
	
	
	return time



@app.route("/",methods=['POST','GET'])
def main():
	pass
	flag = 0
	
	if request:
		
		url = "http://192.168.2.1:5002"
		
		data = request.get_json(silent=True)
		print(data)
		
		data['detect_time'] = Face_Detect()

		data = re.post(url,headers=headers,data=json.dumps(data)).json()
		
		return data

	


if __name__ == "__main__":
	app.run(host="192.168.2.1",port=5001,threaded=True)
