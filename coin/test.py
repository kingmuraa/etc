import requests

url = "https://api.bithumb.com/public/ticker/GALA_KRW"
resp = requests.get(url)
data = resp.json()

print(data['data']['opening_price'])

# print(data)