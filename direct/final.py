from time import sleep
from PIL import Image
import requests
import base64
import shutil
import json
import os




# ================= START COLOR TEXT =================
credg = '\33[92m'
credy = '\33[33m'
credr = '\33[91m'
cend = '\33[0m'
# ================= END COLOR TEXT =================



# LOGIN DODOLANS
print()
print(f'{credy}Mengecek Token...{cend}')
print()
sleep(2)

if os.path.exists('session/token.txt'):
	print(f"{credg}Token ditemukan{credg}")
	sleep(1)
	print("Login dilewat")
	sleep(1)

else:
	print (f"{credr}Token tidak ditemukan{cend}")
	print()
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

	dumps = json.dumps(rLogin.json())
	token = json.loads(dumps)['token']

	try:
		os.mkdir('session')
	except:
		pass

	with open('session/token.txt', 'w') as file:
		file.write(token)
		file.close
	print(f'{credg}Token tersimpan di session/token.txt{cend}')

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

print(f'└─ Grabing Data Status : {credg}{rGrab.status_code}{cend}')
sleep(1)
dumps = json.dumps(rGrab.json(), indent = 3)

try:
	os.mkdir('data')
except:
	pass
with open('data/data.json', 'w') as file:
	file.write(dumps)
	file.close
print(f'{credg}Data Merchant tersimpan di data/data.json\n{cend}')
sleep(1)



# CREATE PLACE

token = open('session/token.txt').read()
merchant = json.load(open('data/data.json'))

# START LIST HOUR
day = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

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

########## WARNING
print(f"Nama Merchant : {merchant['merchant']['name']}")
print(f"Deskripsi : {merchant['merchant']['description']}")
print(f"Kategori : {merchant['merchant']['cuisine']}")

########## REQUESTS
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


parent = ""

rCreate = requests.post(urlCreate, data=bodyCreate)

print()
print(f"{credy}Create Place{cend}")
print()
print(f"┌─[+]Input Merchant {merchant['merchant']['name']} Berhasil | Status : {credg}{rCreate.status_code}{cend}")
sleep(1)
loadsss = json.loads(json.dumps(rCreate.json()))
response = loadsss['error']
parent = loadsss['list']['view_uid']
print(f'├──[Error] {response}')
sleep(1)
	

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

print(f'└─┬─[+] Upload Image Status :  {credg}{Upload.status_code}{cend}') # response status code
sleep(1)
response = json.loads(json.dumps(rUpload.json()))['error']
print('  └─[Error]', response) # response json
sleep(1)
print()
 

# CREATE PRODUCT

print('┌─[ID Kecamatan]')
print('├──[10] Pekalongan Barat')
print('├──[11] Pekalongan Selatan')
print('├──[12] Pekalongan Timur')
print('├──[13] Pekalongan Utara')
district = f"49{input('└─── ID Kecamatan : ')}"
print()
sleep(1)
categories = merchant['merchant']['menu']['categories']

listLinkImg = []
for z in range(len(categories)):
	items = categories[z]['items']
	try :
		for x in range(len(items)):
			listLinkImg.append(items[x]['imgHref'])
	except :
		pass

print(f"{credy}Encoding Image to base64{cend}")
print()
listBase64Img = []

for w in listLinkImg:
	if w == "":
		enc_img = image
	else:
		rGetImg = requests.get(w)
		file = open("data/img.webp", "wb")
		file.write(rGetImg.content)
		file.close()

		im = Image.open("data/img.webp").convert("RGB")
		im.save("data/img.jpg", "jpeg")

		with open("data/img.jpg", "rb") as file:
			b64_string = base64.b64encode(file.read())

		enc_img = str(b64_string.decode('utf-8'))
		print(f"Encode Image {listLinkImg.index(w)} | Status : {credg}{rGetImg.status_code}{cend}")
		os.remove("data/img.jpg")

	listBase64Img.append(enc_img)
print()

iterImgBase64 = iter(listBase64Img)


print(f"{credy}Create Product{cend}")
print()
for n in range(len(categories)):
	try:
		items = categories[n]['items']
		for i in range(len(items)):
			urlProduct = "https://www.jagel.id/api/v3/partner/create_product.php"

			price = items[i]['discountedPriceV2']['amountDisplay'].replace('.', '')
			discountedPrice = round(int(price) - (int(price) * 20 / 100))

			np = items[i]['name']
			filt0 = np.replace("✕", "X")
			filt1 = filt0.replace(".", " ")
			filt2 = filt1.replace(",", " ")
			filt3 = filt2.replace("+", " ")
			filt4 = filt3.replace("/", " atau ")
			filt5 = filt4.replace("(", " ")
			filt6 = filt5.replace(")", " ")
			filt7 = filt6.replace("   ", " ")
			nameProduct = filt7.replace("  ", " ")


			if items[i]['description'] == "":
				desc = "Permintaanmu akan disesuaikan dengan kebijakan resto"
			else :
				desc = items[i]['description']

			bodyProduct = {
				"title": nameProduct, # perlu ubah
				"content": desc, # perlu ubah
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

			rProduct = requests.post(urlProduct, data=bodyProduct)

			print(f"┌─[+] Input {items[i]['name']} Berhasil | Status : {credg}{rProduct.status_code}{cend}")
			print("├──[Error] ", json.loads(json.dumps(rProduct.json()))['error'])

			# UPLOADE IMAGE
			dumps = json.dumps(rProduct.json())
			loads = json.loads(dumps)
			view_uid = loads['list']['view_uid']
			title = loads['list']['title']
			urlProduct_Upload = 'https://www.jagel.id/api/v3/partner/upload_image.php'

			try : 
				bodyProduct_Upload = {
					"image": next(iterImgBase64), #PerluDiubah
					"hl": "in",
					"view_uid": view_uid,
					"appuid": "5f3e3c3c77909",
					"position": "0",
					"title": title,
					"token": token,
					"image_type": "jpg"
				}

				rProduct_Upload = requests.post(urlProduct_Upload, data=bodyProduct_Upload)

				print(f'└─┬─[+] Upload Image Status :  {credg}{rProduct_Upload.status_code}{cend}') # response status code
				sleep(1)
				response = json.loads(json.dumps(rProduct_Upload.json()))['error']
				print('  └─[Error]', response) # response json
				sleep(1)
				print()
			except :
				pass
	except:
		print(f'{credr}Item tidak ditemukan di kategori {n}{cend}')

print(f"Total Produk : {len(listLinkImg)}")
shutil.rmtree("data")

