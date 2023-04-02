import requests

url = 'http://localhost:5000/process_data'
data = {'key': 'value'}
#response = requests.post(url, json=data)

#print(response.json())
print(requests.head("https://else.fcim.utm.md"))