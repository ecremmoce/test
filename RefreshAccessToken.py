# refresh token


def get_access_token_shop_level(shop_id, partner_id, tmp_partner_key, refresh_token):
    timest = int(time.time())
    host = "https://partner.test.shopeemobile.com"
    path = "/api/v2/auth/access_token/get"
    body = {"shop_id": shop_id, "refresh_token": refresh_token,"partner_id":partner_id}
    tmp_base_string = "%s%s%s" % (partner_id, path, timest)
    base_string = tmp_base_string.encode()
    partner_key = tmp_partner_key.encode()
    sign = hmac.new(partner_key, base_string, hashlib.sha256).hexdigest()
    url = host + path + "?partner_id=%s&timestamp=%s&sign=%s" % (partner_id, timest, sign)
    # print(url)
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, json=body, headers=headers)
    ret = json.loads(resp.content)
    access_token = ret.get("access_token")
    new_refresh_token = ret.get("refresh_token")
    return access_token, new_refresh_token


def get_access_token_merchant_level(merchant_id, partner_id, tmp_partner_key, refresh_token):
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
    return access_token, new_refresh_token

partner_id = 2006566
partner_key = "1a78dde5d6c3342f56ac939cbdd81607654c0e87725e118736ba5e3ae31c579c"
shop_id = 602226924
main_account_id = 31219
merchant_id = 45719
code = "c01204cada7b4cd0e4688154f5a256ca"
#access_token,refresh_token = get_token_shop_level(code,partner_id,partner_key,602226924)
print(access_token)
print(refresh_token)
print(get_access_token_shop_level(shop_id,partner_id,partner_key,refresh_token))


#access_token,refresh_token = get_token_account_level(code,partner_id,partner_key,main_account_id)
print(access_token)
print(refresh_token)
print(get_access_token_merchant_level(merchant_id,partner_id,partner_key,refresh_token))