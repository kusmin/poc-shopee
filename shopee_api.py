import hashlib
import hmac
import time
import requests
from urllib.parse import urlencode

from config import PARTNER_ID, PARTNER_KEY, BASE_URL, AUTH_URL

def generate_sign(path, params):
    base_string = f"{path}|{PARTNER_ID}|{params['timestamp']}|{params.get('access_token', '')}|{params.get('shop_id', '')}"
    if 'merchant_id' in params:
        base_string = f"{path}|{PARTNER_ID}|{params['timestamp']}|{params.get('access_token', '')}|{params.get('merchant_id', '')}"
    elif 'access_token' not in params and 'shop_id' not in params and 'merchant_id' not in params:
        base_string = f"{path}|{PARTNER_ID}|{params['timestamp']}"

    sign = hmac.new(PARTNER_KEY.encode(), base_string.encode(), hashlib.sha256).hexdigest()
    return sign

def generate_auth_link(redirect_url):
    path = "/api/v2/shop/auth_partner"
    timestamp = int(time.time())
    params = {
        "partner_id": PARTNER_ID,
        "timestamp": timestamp,
        "redirect_url": redirect_url
    }
    sign = generate_sign(path, params)
    params["sign"] = sign
    
    query_string = urlencode(params)
    return f"{AUTH_URL}?{query_string}"

def get_access_token(main_account_id, code):
    path = "/api/v2/auth/token/get"
    timestamp = int(time.time())
    
    body = {
        "partner_id": PARTNER_ID,
        "main_account_id": main_account_id,
        "code": code,
        "timestamp": timestamp
    }
    
    sign = hmac.new(PARTNER_KEY.encode(), (path + '|' + str(PARTNER_ID) + '|' + str(timestamp)).encode(), hashlib.sha256).hexdigest()
    
    headers = {
        "Content-Type": "application/json"
    }
    
    url = f"{BASE_URL}{path}?partner_id={PARTNER_ID}&timestamp={timestamp}&sign={sign}"
    
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()
    return response.json()

def refresh_access_token(shop_id, refresh_token):
    path = "/api/v2/auth/token/refresh"
    timestamp = int(time.time())
    
    body = {
        "partner_id": PARTNER_ID,
        "shop_id": shop_id,
        "refresh_token": refresh_token,
        "timestamp": timestamp
    }
    
    sign = hmac.new(PARTNER_KEY.encode(), (path + '|' + str(PARTNER_ID) + '|' + str(timestamp)).encode(), hashlib.sha256).hexdigest()
    
    headers = {
        "Content-Type": "application/json"
    }
    
    url = f"{BASE_URL}{path}?partner_id={PARTNER_ID}&timestamp={timestamp}&sign={sign}"
    
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()
    return response.json()

def make_api_call(path, access_token, shop_id, params=None):
    timestamp = int(time.time())
    
    if params is None:
        params = {}
    
    params.update({
        "partner_id": PARTNER_ID,
        "timestamp": timestamp,
        "access_token": access_token,
        "shop_id": shop_id
    })
    
    sign = generate_sign(path, params)
    params["sign"] = sign
    
    query_string = urlencode(params)
    url = f"{BASE_URL}{path}?{query_string}"
    
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


