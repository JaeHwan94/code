from flask import Flask,request
import requests as re
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random
from datetime import datetime as dt
import json
import time

app = Flask(__name__)

def End_Time():
	now = dt.now()

	time = {'month':now.month,'day':now.day,'hour':now.hour,'min':now.minute,'sec':now.second}

	data = "{}m-{}d-{}h-{}m-{}s".format(time['month'],time['day'],time['hour'],time['min'],time['sec'])

	return data,time

def Push_Data(data): 
	
	m_data = data['A']

	m_data['member_verify_time_b'] = data['B']['member_verify_time_b']

	if m_data['member_group'] == "N":
		m_data = data['B']

		m_data = data['A']['member_verify_time_a']
	
	time = m_data['detect_time']+m_data['extract_time']+m_data['member_verify_time_a']+m_data['member_verify_time_b']
	m_data['end_time'],time = End_Time()
    #prometheus gateway metric
	registry = CollectorRegistry()

	g = Gauge('Processing_All_Info','All information about the processing process',['member_name','member_group','detect_time','extract_time','member_verify_time_a','member_verify_time_b','start_time'
	,'end_time'],registry=registry)

	g.labels(member_name=m_data['member_name'],member_group=m_data['member_group'],detect_time=m_data['detect_time'],extract_time=m_data['extract_time'],member_verify_time_a=m_data['member_verify_time_a'],
			 member_verify_time_b=m_data['member_verify_time_b'], start_time = m_data['start_time'] , end_time = m_data['end_time']	)

	push_to_gateway('http://192.168.2.1:9092',job='Face_App_Process_Info',registry=registry)

	#process end time
	registry = CollectorRegistry()
	g = Gauge('Process_End_Time','Prcess end time',['start_time','end_time'],registry=registry)
	g.labels(start_time=m_data['start_time'],end_time=m_data['end_time']).set(time['min'])
	push_to_gateway('http://192.168.2.1:9092',job='Check_End_Time',registry=registry)

_url = "http://"
member_data = {}
count = 0
@app.route("/",methods=['POST','GET'])
@app.route("/a",methods=['POST','GET'])
def Check_A():
	pass
	global count
	global member_data
	
	if request:
		data = request.get_json(silent=True)
		if count < 2:
			member_data['A'] = data
			count += 1

		if count >= 2:
			Push_Data(member_data)
			count = 0
			member_data = {}

		return "OK"
		
@app.route("/b",methods=['POST','GET'])
def Check_B():
	global count
	global member_data

	if request:
		time.sleep(10)
		data = request.get_json(silent=True)
		if count < 2:
			member_data['B'] = data
			count += 1

		if count >= 2:
			Push_Data(member_data)
			count = 0
			member_data = {}
		
		return "OK"


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000,threaded=True)
