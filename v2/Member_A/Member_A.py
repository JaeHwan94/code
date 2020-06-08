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
	g = Gauge('Face_Member_Check_A',"Member's Face check processing time - A Group",registry=registry)
	g.set(data)
	push_to_gateway('http://192.168.2.1:9092',job='Face_Member_Checker_A',registry=registry)


def Member_Verify(data):
	time = random.randint(30,120)
	
	m_data = {'member_verify_time':0,'member':'','member_name':'Not Member'}

	m_data['member_verify_time'] = time

	mem = random.randint(0,2)

	if mem == 0:
		m_data['member_group'] = "A"
		m_data['member_name'] = "Member%d"%(random.randint(1,100))
	else:
		m_data['member_group'] = "N"
	
	return m_data


_url = "http://"
headers = {'Content-Type':'application/json'}
@app.route("/",methods=['POST','GET'])
def main():
	pass
	flag = 0
	
	if request:
		
		url = _url+"ai-model-repository:5000"
		data = re.post(url)

		m_data = Member_Verify(data)
		
		data = request.get_json(silent=True)
		data['member_verify_time_a'] = m_data['member_verify_time']
		data['member_group'] = m_data['member']
		data['member_name'] = m_data['member_name']

		url = _url+"member-check:5000/a"
		re.post(url,headers=headers,data=json.dumps(data))
		
		Push_Data(data['member_verify_time_a'])

		return "OK"
	


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000,threaded=True)
