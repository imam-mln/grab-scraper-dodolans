import requests
import json

image = open('data/image.txt', 'r').read()
url = 'https://www.jagel.id/api/v3/partner/upload_image.php'
body = {
	"image": image,
	"hl": "in",
	"view_uid": "62ca2d75007cf",
	"appuid": "5f3e3c3c77909",
	"position": "0",
	"title": "Bubur+Ayam+Faiz+-+Sapuro+Kebulen",
	"token": "d996af9efa5aefaa2eac4a374e6f03b4",
	"image_type": "jpg"
}

# print(img[0])
# r = requests.post(url, headers=head, json=body)

# print(r.status_code)
# print()
# print(r.json())


print(body)