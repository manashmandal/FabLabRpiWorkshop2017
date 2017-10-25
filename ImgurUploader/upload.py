import requests

album_id = "BxTED"

client_id = "772f8ccdb6652ee"
client_secret = "376c2cd99e931b278347d143414e212dbdbde5af"

endpoint = "https://api.imgur.com/3/image"

from requests_toolbelt.multipart.encoder import MultipartEncoder

m = MultipartEncoder(
    fields={'title': 'Raspberry Pi Logo',
            'image': open('raspberry-pi-logo.png', 'rb')}
    )


headers = {'authorization' : 'Client-ID ' + client_id, 'Content-Type' : m.content_type }

response = requests.request('POST', endpoint, data=m, headers=headers)

print(response.text)

