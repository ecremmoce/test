import hmac
import json
import time
import requests
import hashlib


def shop_auth():
    timest = int(time.time())
    host = "https://partner.shopeemobile.com"
    path = "/api/v2/shop/auth_partner"
    redirect_url = "https://www.acsell.ai"
    partner_id = 846699
    tmp = "d6a599b842631283fdd24dd204550e4d14f76fbadb4dc77d786e7ab1b9ec7b46"
    partner_key = tmp.encode()
    tmp_base_string = "%s%s%s" % (partner_id, path, timest)
    base_string = tmp_base_string.encode()
    sign = hmac.new(partner_key, base_string, hashlib.sha256).hexdigest()
    ##generate api
    url = host + path + "?partner_id=%s&timestamp=%s&sign=%s&redirect=%s" % (partner_id, timest, sign, redirect_url)
    print(url)