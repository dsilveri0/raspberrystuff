import requests
from datetime import datetime

def post(auxInputTemp):
	paramUrl = 'http://192.168.43.87/api/lab04_api_post_json_switch.php'
	paramAuth = 'irsotesppsi'
	paramKey = 'switch'
	paramNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	paramJSON = {'auth':paramAuth, 'key':paramKey, 'value':auxInputTemp, 'date':paramNow}
	paramHeaders = {'content-type': 'application/json'}

	r = requests.post(paramUrl, json=paramJSON, headers=paramHeaders)
