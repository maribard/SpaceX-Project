import requests

BASE = "http://127.0.0.1:5000/"

#[('B1049', 6, 91880), ('B1051', 5, 75274),


response = requests.put(BASE + "cores/" + "B123", {"reuse_count": 6, "payload_mass": 45657})
#print(response.json())

input()

response = requests.get(BASE + "cores/B123")
