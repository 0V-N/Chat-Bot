import requests

url = 'http://localhost:5000/chat'  # Replace with your API endpoint URL
headers = {
    'Content-Type': 'application/json'
}
data = {
    'message': 'Hello'
}

response = requests.post(url, headers=headers, json=data)
