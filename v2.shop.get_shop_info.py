import requests
import requests
import hmac 
import time
import hashlib
import ssl
import json
import urllib3
import clipboard

#shop의 정보를 알아낸다.

timestamp = int(time.time())
host = "https://partner.shopeemobile.com"
path = "/api/v2/shop/get_shop_info"
tmp = "d6a599b842631283fdd24dd204550e4d14f76fbadb4dc77d786e7ab1b9ec7b46"
partner_id = 846699
access_token ="4d4f4c75707a664a4e4c476c68647354"
shop_id = 194181449
partner_key = tmp.encode()
tmp_base_string = "%s%s%s%s%s" % (partner_id, path, timestamp,access_token, shop_id)
base_string = tmp_base_string.encode()
sign = hmac.new(partner_key, base_string, hashlib.sha256).hexdigest()

url = "https://partner.shopeemobile.com/api/v2/shop/get_shop_info?access_token=%s&partner_id=%d&shop_id=%d&sign=%s&timestamp=%s" % (access_token,partner_id, shop_id, sign, timestamp)

payload={}
headers = {

}
print(url)
response = requests.request("GET",url,headers=headers, data=payload, allow_redirects=False)
ret = json.loads(response.content)
print(ret["shop_cbsc"])
clipboard.copy(response.content.decode())
print(response.text)
print("Say Hello")
print('Good Boy')