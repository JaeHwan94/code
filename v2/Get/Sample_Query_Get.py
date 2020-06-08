import requests as re
import json


_url = "http://"

def Get_Data(query):
	ip = "192.168.2.1:"
	port = "82"
	end_point = "/api/v1/query"
	url = _url+ip+port+end_point
	data = re.get(url,params={"query":query}).json()


	return data['data']['result'][0]['metric']

def Calc_Processing_Time(start,end):
	start = start.split('-')

	end = end.split('-')
	
	s = 1
	m = s*60
	h = m*60
	time = [h,m,s]

	processing_time = 0

	print(start)
	print(end)

	for i in range(len(start)):
		processing_time +=(int(end[i][:-1])-int(start[i][:-1]))*time[i]
	
	return processing_time

def main():
	start_time_query = "Process_Start_Time"

	start_time = Get_Data(start_time_query)['start_time']

	end_time_query = "Process_End_Time{start_time='%s'}"%(start_time)

	end_time = Get_Data(end_time_query)
		
		
	print(Calc_Processing_Time(end_time['start_time'],end_time['end_time']))
	
	


if __name__ == "__main__":
	main()	 




