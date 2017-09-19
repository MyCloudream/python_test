import requests
import json

form = {'username': 'cloud', 'password': '123456'}
res = requests.post('http://httpbin.org/post', data=form)
print(res.text)
res = requests.post('http://httpbin.org/post', data=json.dumps(form))
print(res.text)
