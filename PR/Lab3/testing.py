import json
import requests

print(requests.options('http://localhost:5000/get_options').headers.get('Access-Control-Allow-Methods'))