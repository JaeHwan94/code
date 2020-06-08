from flask import Flask,render_template,request
import requests as re
import json

app = Flask(__name__,template_folder='templates')

_url = "http://"

def Get_Data():
	query = "Processing_All_Info"
	ip = "192.168.2.1:"
	port = "82"
	end_point = "/api/v1/query"
	url = _url+ip+port+end_point
	data = re.get(url,params={"query":query}).json()

	return data['data']

@app.route("/get",methods=['GET','POST'])
def main():
	data = {}
	global _url

	
	if request:
		data = Get_Data()
		
		info = data['result'][0]

		return info
	


if __name__ == "__main__":
	 

	app.run(host="0.0.0.0",port=5000, threaded=True)



