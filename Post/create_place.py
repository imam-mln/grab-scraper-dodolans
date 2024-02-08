import requests
import json

# LOAD DATA MERCHANT GRAB
son = open('data/data.json')
data = json.load(son)

# TOKEN LOGIN DODOLANS
token = input('token : ')

# CREATE PLACE
url_create_place = 'https://www.jagel.id/api/v3/partner/create_place.php'

print("\nMerchant : " + data['merchant']['name'])
print('Jika tutup input 0, jika buka input 1\nJika tutup, jam & menit input -1\n')
print('Label tersedia : cafe, mie dan bakso, warung, minuman, mie, sarapan, jajanan, promo, penyetan, kue, 24jam, terlaris, jamu, oleh, toko, pakaian, buah, sayur, sembako, satenasgor\n')

bodyCP = {
  "token": token,
  "component_view_uid": '6215d6e509e7f',
  "title": data['merchant']['name'],
  "content": data['merchant']['cuisine'],
  "label": f"{input('Label : ')}",
  "origin_address": data['merchant']['address']['combined_address'],
  "origin_lat": data['merchant']['latlng']['latitude'],
  "origin_lng": data['merchant']['latlng']['longitude'],
  "day_1": f"{input('########## Senin : ')}",
  "day1_start_hour": f"{input('# Jam buka : ')}",
  "day1_start_minute": f"{input('Menit : ')}",
  "day1_end_hour": f"{input('# Jam tutup : ')}",
  "day1_end_minute": f"{input('Menit : ')}",
  "day_2": f"{input('########## Selasa : ')}",
  "day2_start_hour": f"{input('# Jam buka : ')}",
  "day2_start_minute": f"{input('Menit : ')}",
  "day2_end_hour": f"{input('# Jam tutup : ')}",
  "day2_end_minute": f"{input('Menit : ')}",
  "day_3": f"{input('########## Rabu : ')}",
  "day3_start_hour": f"{input('# Jam buka : ')}",
  "day3_start_minute": f"{input('Menit : ')}",
  "day3_end_hour": f"{input('# Jam tutup : ')}",
  "day3_end_minute": f"{input('Menit : ')}",
  "day_4": f"{input('########## Kamis : ')}",
  "day4_start_hour": f"{input('# Jam buka : ')}",
  "day4_start_minute": f"{input('Menit : ')}",
  "day4_end_hour": f"{input('# Jam tutup : ')}",
  "day4_end_minute": f"{input('Menit : ')}",
  "day_5": f"{input('########## Jumat : ')}",
  "day5_start_hour": f"{input('# Jam buka : ')}",
  "day5_start_minute": f"{input('Menit : ')}",
  "day5_end_hour": f"{input('# Jam tutup : ')}",
  "day5_end_minute": f"{input('Menit : ')}",
  "day_6": f"{input('########## Sabtu : ')}",
  "day6_start_hour": f"{input('# Jam buka : ')}",
  "day6_start_minute": f"{input('Menit : ')}",
  "day6_end_hour": f"{input('# Jam tutup : ')}",
  "day6_end_minute": f"{input('Menit : ')}",
  "day_7": f"{input('########## Minggu : ')}",
  "day7_start_hour": f"{input('# Jam buka : ')}",
  "day7_start_minute": f"{input('Menit : ')}",
  "day7_end_hour": f"{input('# Jam tutup : ')}",
  "day7_end_minute": f"{input('Menit : ')}",
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

y = "y"

if input('\nLanjut? input y : ') == y:
  print('\nCreate Place')
  requestsCP = requests.post(url_create_place, data=bodyCP)

  # REQUEST CREATE PLACE STARTED
  print('Status : ', requestsCP.status_code)
  responseCP = json.dumps(requestsCP.json(), indent=3)
  print(responseCP)
  print()

  # UPLOAD IMAGE
  load = json.loads(responseCP) # ambil response object dari create_place
  view_uid = load['list']['view_uid'] # view_uid dari response create_place
  title = load['list']['title'] # title dari response create_place

  # LOAD IMAGE DODOLANS BASE64
  image = open('data/image.txt', 'r').read() # string

  url_upload_image = 'https://www.jagel.id/api/v3/partner/upload_image.php'
  bodyUI = {
    "image": image,
    "hl": "in",
    "view_uid": view_uid,
    "appuid": "5f3e3c3c77909",
    "position": "0",
    "title": title,
    "token": token,
    "image_type": "jpg"
  }

  requestsUI = requests.post(url_upload_image, data=bodyUI)

  # REQUEST UPLOAD IMAGE STARTED
  print('Status : ', requestsUI.status_code) # response status code
  print(requestsUI.json()) # response json

else:
  pass





# Hiraukan
# Data Images
# print()

# with open('response.json', 'w') as file:
#   file.write(json.dumps(r.json(), indent=3))
#   file.close

# rJson = json.load(open('response.json', 'r'))
# rTitle = rJson['list']['title'].replace(' ', '+')

# image = open('image.txt', 'r').read()

# with open('data.txt', 'w') as file:
#   file.write(image)
#   file.close

# asu = f"&hl=in&view_uid={rJson['list']['view_uid']}&appuid=5f3e3c3c77909&position=0&title={rTitle}&token=d996af9efa5aefaa2eac4a374e6f03b4&image_type=jpg&"
# with open('data.txt', 'a') as file:
#   file.write(asu)
#   file.close

# # data = open('data.txt', 'r').read()