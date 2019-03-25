import requests

url = 'hhtp://localhost:5999/api'

r = requests.port(url,json={'exp':1.8,})
print(r.json())
