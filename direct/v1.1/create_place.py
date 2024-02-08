from time import sleep
import requests
import json
import os



# ================= START COLOR TEXT =================
credg = '\33[92m'
credy = '\33[33m'
credr = '\33[91m'
cend = '\33[0m'
# ================= END COLOR TEXT =================



# LOGIN DODOLANS

print(f'{credy}Mengecek Token...{cend}\n')
sleep(2)
if os.path.exists('data/token.txt'):
	print(f"{credg}Token ditemukan{credg}\n")
	sleep(1)
	print("Login dilewat")
	sleep(1)
else:
	print (f"{credr}Token tidak ditemukan{cend}\n")
	sleep(1)
	print('Login')
	sleep(1)
	urlLogin = "https://www.jagel.id/api/v3/basic/login.php"
	bodyLogin = {
		"username": input('Username : '),
		"password": input('Password : '),
		"hl": 'in',
		"imei": '7154624f6161616150737859516746456847634c506c7376536e797064446800',
		"appuid": '5f3e3c3c77909',
		"firebase_token": 'e6Gwmju3S9WOQZq8MfvsCX:APA91bGgTAnMH9dx2UVhfYUqSKlc4Di_BhkcelLYqNb0Rv6WYsCLul8KJjKbESgQ4WimRiGAIamc2rgeU0AdAopv1LprwwuP3Dl8xhS3-asvYP8j5MyGZzSfGVLunzyuDcR22ZASinab',
		"firebase_type": '1'
	}
	rLogin = requests.post(urlLogin, data = bodyLogin)

	print(f'Login Status : {credg}{rLogin.status_code}{cend}')

	dumps = json.dumps(rLogin.json(), indent=3)
	token = json.loads(dumps)['token']
	try:
		os.mkdir('data')
	except:
		pass
	with open('data/token.txt', 'w') as file:
		file.write(token)
		file.close
	print(f'{credg}Token tersimpan di data/token.txt{cend}')



# GET DATA MERCHANT FROM GRABFOOD

print(f"\n{credy}Grabing Data Merchant From GrabFood{cend}\n")
sleep(1)
urlGrab = f'https://p.grabtaxi.com/api/passenger/v4/grabfood/merchants/{input("ID Merchant : ")}?latlng=-6.890702%2C109.676352'
headGrab = {
	"x-request-id": "7213abd6-3ed8-43d9-90e9-095bbb47d893",
	"Accept-Language": "in-ID;q=1.0, en-US;q=0.9, en;q=0.8",
	"User-Agent": "Grab/5.204.0 (Android 11; Build 34436267)",
	"x-mts-ssid": "eyJhbGciOiJSUzI1NiIsImtpZCI6Il9kZWZhdWx0IiwidHlwIjoiSldUIn0.eyJhdWQiOiJQQVNTRU5HRVIiLCJlc2kiOiJrT1AvTGtPNitYLzltVTJYbGtmTHllVVdLSC9QdzhKL2tyRXNqYlArR2RabjMwL0tyUT09IiwiZXhwIjo0ODA4NzEwMjc2LCJpYXQiOjE2NTUxMTAyNzMsImp0aSI6Ijg2NTBhMTgxLTMwNjEtNDk0NC1iM2QzLTAxNWNlZDExYTA3NSIsImxtZSI6IkdPT0dMRVYzIiwibmFtZSI6IiIsInN1YiI6ImIxNTRiODVkLTYzMDAtNGJmMS05MTBmLWJjNjAyN2M1ZGRjYiJ9.uJeQmWXcUaXFK8S51zvoQjA4bfpl02KHJ6UYIMqo_fXRXFzi6gDc-Gqe4m2pdmN5iS1wmFXtGiUSEztQol-e1NtLlTLDTroYHzVAbCLZcsnwhlTvk2gz48Esy8MwF5pZ89u2JHN3aFl8pyXmLYyI-tg-JHpEiUoLQ82Kuu8lXXZioMUJgbGalr2-WZqnrUgQo0tRfkGVWn32z03W4LYQ856pIpy5TBUIiOWyfVQ991Fxb3WjmXhBhQhJXOcHBxXQqAInqZeLx5WCEQsUEYMgCPTigwY3pbFuhA9x37Ge1YvLGf88_zTQILc2u7P_L-0yMeqEGbPHHu-i8fi7DRqdudhQxUlw_KvQtOS_D0AtLqGlz5Gwx2y_ZxLIbSUhwok26lPlMDRfqQvPFKF7KnqH9PBL3PGxJDMmhTKbaxo538nQa_yf9uhx3ydmVHsk_oTvx79qyeuNKYsVVsBv5lyywnnIfASTONC1EKOVGEroCCScnwtwHos2hz51b_nk47N8d_3DT9p5FSyxkOuzZSBe7fdsBHHysQUaoUOa5U736dyuTdHCjtk-lKp80MzcHoeVNQofJolg7kXKVxdToBH2leuVNE_Irz9FnL0OIFzHqtpFDH5WDF78EraYoo9JlUPmkdfHQ4zWFP6ujhRawmZGwPGk5tlk8BePNzuJ3iRutg8",
	"Host": "p.grabtaxi.com",
	"Connection": "close",
	"Accept-Encoding": "gzip, deflate"
}

rGrab = requests.get(urlGrab, headers = headGrab)

print(f'Status : {credg}{rGrab.status_code}{cend}')
sleep(1)
dumps = json.dumps(rGrab.json(), indent = 3)
with open('data/data.json', 'w') as file:
	file.write(dumps)
	file.close
print(f'{credg}Data Merchant tersimpan di data/data.json\n{cend}')
sleep(1)



# CREATE PLACE

token = open('data/token.txt').read()
merchant = json.load(open('data/data.json'))

# START LIST HOUR
day = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

listHour = []
idx = 1

for i in day:
	ex = []
	hour = merchant['merchant']['openingHours'][i]
	txt = hour.split("-")
	if len(txt) == 1:
		listHour.append(txt)
	else:
		sh_sm = txt[0].split(':')
		eh_em = txt[1].split(':')
		ex.append(sh_sm)
		ex.append(eh_em)
		listHour.append(ex)
# print(listHour)
# END LIST HOUR

urlCreate = 'https://www.jagel.id/api/v3/partner/create_place.php'
bodyCreate = {
  "token": token, # PERHATIKAN TOKEN AKUN!
  "component_view_uid": '6215d6e509e7f',
  "title": merchant['merchant']['name'],
  "content": merchant['merchant']['cuisine'],
  "label": input('Label : '),
  "origin_address": merchant['merchant']['address']['combined_address'],
  "origin_lat": merchant['merchant']['latlng']['latitude'],
  "origin_lng": merchant['merchant']['latlng']['longitude'],
  "hl": 'in',
  "working_hour": '0',
  "hide_image_flag": '0',
  "by_appointment": '0',
  "set_origin_flag": '1',
  "style": '0',
  "purchasable": '0',
  "price": '0',
  "appuid": '5f3e3c3c77909'
}

# START ADD DICTIOMARY HOUR
for j in listHour:
	if len(j) < 2:
		bodyCreate[f"day_{idx}"] = 0
		bodyCreate[f"day{idx}_start_hour"] = -1
		bodyCreate[f"day{idx}_start_minute"] = -1
		bodyCreate[f"day{idx}_end_hour"] = -1
		bodyCreate[f"day{idx}_end_minute"] = -1
	else:
		bodyCreate[f"day_{idx}"] = 1
		bodyCreate[f"day{idx}_start_hour"] = j[0][0]
		bodyCreate[f"day{idx}_start_minute"] = j[0][1]
		bodyCreate[f"day{idx}_end_hour"] = j[1][0]
		bodyCreate[f"day{idx}_end_minute"] = j[1][1]
	idx += 1
# START ADD DICTIOMARY HOUR

print("\n" + f"{credy}Nama Merchant '{merchant['merchant']['name']}'{cend}")
print("Apakah anda yakin input merchant ini?")
confirm = str.lower(input(f"{credg}[y]Yes{cend} or {credr}[n]No{cend} : "))

parent = ""
if confirm == "y":
  rCreate = requests.post(urlCreate, data=bodyCreate)

  print()
  print(f"(+) Input Merchant {merchant['merchant']['name']} Berhasil | Status : {credg}{rCreate.status_code}{cend}")
  sleep(1)
  loadsss = json.loads(json.dumps(rCreate.json()))
  response = loadsss['error']
  parent = loadsss['list']['view_uid']
  print(f'   Error : {response}')
  print()
  sleep(1)
else:
  pass




# UPLOADE IMAGE
dumps = json.dumps(rCreate.json())
loads = json.loads(dumps)
view_uid = loads['list']['view_uid']
title = loads['list']['title']
image = open('dodolanImage.txt', 'r').read() # string

urlUpload = 'https://www.jagel.id/api/v3/partner/upload_image.php'
bodyUpload = {
	"image": image,
	"hl": "in",
	"view_uid": view_uid,
	"appuid": "5f3e3c3c77909",
	"position": "0",
	"title": title,
	"token": token,
	"image_type": "jpg"
}

rUpload = requests.post(urlUpload, data=bodyUpload)

print('Upload Image Status : ', rUpload.status_code) # response status code
sleep(1)
response = json.loads(json.dumps(rUpload.json()))['error']
print('Error :', response) # response json
sleep(1)
print('\nDone')



# CREATE PRODUCT

print('\nID Kecamatan Tersedia :')
print('Pekalongan Barat : 10')
print('Pekalongan Selatan : 11')
print('Pekalongan Timur : 12')
print('Pekalongan Utara : 13')
print()
district = f"49{input('ID Kecamatan : ')}"
print()
categories = merchant['merchant']['menu']['categories']
for n in range(len(categories)):
	try:
		items = categories[n]['items']
		for i in range(len(items)):
			urlProduct = "https://www.jagel.id/api/v3/partner/create_product.php"

			price = items[i]['discountedPriceV2']['amountDisplay'].replace('.', '')
			discountedPrice = round(int(price) - (int(price) * 20 / 100))

			bodyProduct = {
				"title": items[i]['name'], # perlu ubah
				"content": items[i]['description'], # perlu ubah
				"label": '', # perlu ubah
				"price": discountedPrice, # perlu ubah
				"quantity": '10',
				"weight": '300', 
				"province": '10', # perlu ubah
				"city": '349', # perlu ubah
				"district": district, # perlu ubah
				"purchasable": '1',
				"price_before_discount": '',
				"text_quantity": '',
				"use_variant": '0',
				"hl": 'in',
				"component_view_uid": '6215d6e509e7f', 
				"parent_view_uid": parent, # respon dari create place
				"appuid": '5f3e3c3c77909',
				"token": token # perlu ubah
			}
			# print(items[i]['name'])

			rProduct = requests.post(urlProduct, data=bodyProduct)
			print(f"(+)Input {items[i]['name']} Berhasil | Status : {rProduct.status_code}")
			print("    Error : ", json.loads(json.dumps(rProduct.json()))['error'])

			# UPLOADE IMAGE
			dumps = json.dumps(rProduct.json())
			loads = json.loads(dumps)
			view_uid = loads['list']['view_uid']
			title = loads['list']['title']
			urlProduct_Upload = 'https://www.jagel.id/api/v3/partner/upload_image.php'
			bodyProduct_Upload = {
				"image": image, #PerluDiubah
				"hl": "in",
				"view_uid": view_uid,
				"appuid": "5f3e3c3c77909",
				"position": "0",
				"title": title,
				"token": token,
				"image_type": "jpg"
			}

			rProduct_Upload = requests.post(urlProduct_Upload, data=bodyProduct_Upload)

			print('(*)Upload Image Status : ', rProduct_Upload.status_code) # response status code
			sleep(1)
			response = json.loads(json.dumps(rProduct_Upload.json()))['error']
			print('    Error :', response) # response json
			sleep(1)
			print(f'{credg}Done{cend}')
			print()
	except:
		print(f'{credr}Item tidak ditemukan di kategori {n}{cend}')

