import datetime
import time
import requests
import json
from urllib import quote
import urllib
import base64
import hashlib
import hmac
import random


def generate_nonce(length=16):
    return ''.join([str(random.randint(0, 9)) for i in range(length)])

url = 'https://www.mlepay.com/api/v2/transaction/create'
timestamp = datetime.datetime.fromtimestamp(time.time())
new = timestamp + datetime.timedelta(days=2)
expiry = time.mktime(new.timetuple())

nonce = generate_nonce()


request_body = {
	"receiver_email":"apsolinap@up.edu.ph",
	"sender_email":"test@example.com",
	"sender_name":"Juan dela Cruz",
	"sender_phone":"+6390000000",
	"sender_address":"Blk 1 Lot 2, Sitio Doon, Katabi ng Daan, Pilipinas",
	"amount":100000,
	"currency":"PHP",
	"nonce":nonce,
	"timestamp":int(time.time()),
	"payload":"id-91288481772412",
	"expiry":expiry,
	"description":"White Denim Tee Shirt - Female - Small"}

base_string = 'POST&' + urllib.quote('https://www.mlepay.com/api/v2/transaction/create') + '&' + urllib.quote(json.dumps(request_body))

secret_key = 'ZDk2NTQ5NTgtYTUxYS00ZGIzLThhYmEtYWY2YmMzZjk4NTRlNjEzYzNkM2UtMDEwOS00MDMxLTk1MjctNmZkZWRmNDRhZjgw'
signature = base64.b64encode(hmac.new(secret_key, base_string, hashlib.sha256).digest()).decode()

header ={
	'X-Signature': signature,
	'Cache-Control': 'no-cache',
	'Content-Type': 'application/json'
}
response = requests.post(url, data=json.dumps(request_body), headers=header)
