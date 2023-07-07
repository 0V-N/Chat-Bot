import requests
import json

url = 'http://localhost:5000/chat'
headers = {'Content-Type': 'application/json'}
payload = {'message': 'Hello'}

response = requests.post(url, headers=headers, data=json.dumps(payload))
data = response.json()
response_text = data['response']
print(response_text)
