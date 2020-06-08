from flask import Flask,request
import requests as re
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random
import time
import json

app = Flask(__name__)



_url = "http://"
@app.route("/",methods=['POST','GET'])
def main():
	pass
	flag = 0
	
	if request:
		return "OK"	
		

	


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000,threaded=True)
