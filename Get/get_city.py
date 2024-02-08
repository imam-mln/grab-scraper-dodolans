import requests
import json
import os

url = "https://www.jagel.id/api/v3/rajaongkir/get_city.php"
body = {
	"hl": 'in',
	"city" : '10',
	"token": '29bf19da083fd9733d8785653d0aae1c'
}

r = requests.post(url, data = body)

try:
	os.mkdir('data')
except:
	pass

son = json.dumps(r.json(), indent=3)
with open('data/city.json', 'w') as file:
	file.write(son)
print('List Kota sudah masuk ke folder data!')
