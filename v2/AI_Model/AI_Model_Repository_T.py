from flask import Flask,request
import requests as re
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random
import time
import json

app = Flask(__name__)



_url = "http://"
@app.route("/",methods=['POST'])
def main():
	pass
	flag = 0
	
	if request:
		return "YES"	
		

	


if __name__ == "__main__":
	app.run(host='192.168.2.1',port=5005,threaded=True)
