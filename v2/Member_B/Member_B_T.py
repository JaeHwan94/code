from flask import Flask,request
import requests as re
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random
import time
import json

app = Flask(__name__)

def Member_Verify(data):
	time = random.randint(30,120)
	
	m_data = {'member_verify_time':0,'member':'','member_name':'Not Member'}

	m_data['member_verify_time'] = time

	mem = random.randint(0,2)

	if mem == 0:
		m_data['member'] = "B"
		m_data['member_name'] = "Member%d"%(random.randint(1,100))
	else:
		m_data['member'] = "N"
	
	return m_data


_url = "http://"
@app.route("/",methods=['POST'])
def main():
	pass
	flag = 0
	
	if request:
		
		url = _url+"ai-model-repository:5000"
		data = re.post("http://192.168.2.1:5005")
		m_data = Member_Verify(data)
		
		data = request.get_json(silent=True)
		data['member_verify_time'] = m_data['member_verify_time']
		data['member'] = m_data['member']
		data['member_name'] = m_data['member_name']

		if data['member'] != "N":
			url = _url+"192.168.2.1:5000/end"
			re.post(url)
			return json.dumps(data)
		else:
			return json.dumps(data)
		
		

	


if __name__ == "__main__":
	app.run(host='192.168.2.1',port=5004,threaded=True)
