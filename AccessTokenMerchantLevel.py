import hmac
import json
import time
import requests
import hashlib

shop_id = 194181449 
refresh_token = ""
partner_id = 846699
tmp_partner_key = "d6a599b842631283fdd24dd204550e4d14f76fbadb4dc77d786e7ab1b9ec7b46"

timest = int(time.time())
host = "https://partner.test.shopeemobile.com"
path = "/api/v2/auth/access_token/get"
body = {"merchant_id": merchant_id, "refresh_token": refresh_token}
tmp_base_string = "%s%s%s" % (partner_id, path, timest)
base_string = tmp_base_string.encode()
partner_key = tmp_partner_key.encode()
sign = hmac.new(partner_key, base_string, hashlib.sha256).hexdigest()
url = host + path + "?partner_id=%s&timestamp=%s&sign=%s" % (partner_id, timest, sign)

headers = {"Content-Type": "application/json"}
resp = requests.post(url, json=body, headers=headers)
ret = json.loads(resp.content)
access_token = ret.get("access_token")
new_refresh_token = ret.get("refresh_token")