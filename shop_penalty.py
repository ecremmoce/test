import requests
import hmac 
import time
import hashlib
import ssl
import json
import urllib3
from urllib.request import urlopen

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def shop_auth():
    timest = int(time.time())
    host = "https://partner.shopeemobile.com"
    path = "/api/v2/shop/auth_partner"
    redirect_url = "https://www.ecremmoce.io/"
    partner_id = 846699
    tmp = "d6a599b842631283fdd24dd204550e4d14f76fbadb4dc77d786e7ab1b9ec7b46"
    partner_key = tmp.encode()
    tmp_base_string = "%s%s%s%s%s" % (partner_id, path, timestamp,access_token, shop_id)
    base_string = tmp_base_string.encode()
    sign = hmac.new(partner_key, base_string, hashlib.sha256).hexdigest()
    ##generate api
    url = host + path + "?partner_id=%s&timestamp=%s&sign=%s&redirect=%s" % (partner_id, timest, sign, redirect_url)
    print(url)


partner_id = 846699
shop_id = 194181449


# ssl._create_default_https_context = ssl._create_unverified_context
# accessTokenUrl = "https://dev-web-bff.ecremmoce.io/api/shopee-products/Shops/accessToken?shopId=%d" % (shop_id)

# r = requests.get(url=accessTokenUrl, params="", verify=False)
# access_token = r.content


# timestamp = int(time.time())

# r = requests.get(url=accessTokenUrl, params="", verify=False)
# json_object = json.loads(r.text)
# access_token = r.text.replace('\"','')


partner_key_tmp = "d6a599b842631283fdd24dd204550e4d14f76fbadb4dc77d786e7ab1b9ec7b46"
access_token ="41556568425445766577706551695066"


host = "https://partner.shopeemobile.com"
path = "/api/v2/account_health/shop_penalty"

timestamp = int(time.time())


partner_key = partner_key_tmp.encode()
tmp_base_string = "%s%s%s%s%s" % (partner_id, path, timestamp,access_token, shop_id)
base_string = tmp_base_string.encode()

sign  = hmac.new(partner_key, base_string, hashlib.sha256).hexdigest()


url = host + path + "?access_token=%s&partner_id=%d&shop_id=%d&sign=%s&timestamp=%s" % (access_token, partner_id, shop_id, sign, timestamp)

payload={}
headers = {

}
response = requests.request("GET",url,headers=headers, data=payload, allow_redirects=False)

print(response.text)