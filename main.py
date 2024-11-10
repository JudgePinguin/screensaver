import requests

r = requests.get("http://ip-api.com/json/")
r_json = r.json()

print(r_json['country'])
print(r_json['city'])

print(r_json['lon'])    # ШИРОТА
print(r_json['lat'])    # ДОГОТА