from flask import Flask,request
import requests as re
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random
import time
import json

app = Flask(__name__)

def Face_Extract():
	time = random.randint(30,120)
	
	
	return time


_url = "http://"
headers = {'Content-Type':'application/json'}

@app.route("/",methods=['POST'])
def main():
	pass
	global _url
	if request:
		group = {"A":"member-a:5000","B":"member-b:5000"}
		
		data = request.get_json(silent=True)

		data['extract_time'] = Face_Extract()
		
		url = _url+group['A']
		data_a = re.post("http://192.168.2.1:5003",headers=headers,data=json.dumps(data)).json()
		
		url = _url+group['B']
		data_b = re.post("http://192.168.2.1:5004",headers=headers,data=json.dumps(data)).json()
		
		

		if data_a['member'] != "N":
			data = data_a
			data['member_verify_time'] += data_b['member_verify_time']
			return data
		elif data_b['member'] != "N":
			data = data_b
			data['member_verify_time'] += data_a['member_verify_time']
			return data
		else:
			data = data_a
			data['member_verify_time'] += data_b['member_verify_time']
			re.post("http://192.168.2.1:5000/end")
			return data
		

	


if __name__ == "__main__":
	app.run(host="192.168.2.1",port=5002,threaded=True)
