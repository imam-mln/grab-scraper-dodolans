import requests
import json

url = "https://httpbin.org/post"

data = {
	'error': "False",
	'list': {
		'view_uid': '62ccf7e568f5a',
		'title': 'Gudeg Mb Rita - Poncol',
		'notif_new_list': "0",
		'app_name': 'Dodolans',
		'app_id': "117241"
	}
}

r = requests.post(url, data	=data)

# print(r.json())

rJson = json.dumps(r.json(), indent=3)
data = json.loads(rJson)['headers']['Accept']

print(data)