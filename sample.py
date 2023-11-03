import requests


request = requests.get("http://127.0.0.1:8000/random/99999999")
print(request.json())