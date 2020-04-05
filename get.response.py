import requests

respons_values = requests.get("http://10.0.0.24:5000/ziyotek")
print(respons_values.text)

data = {
    "favorite-character": "IG-11"
    #"lease-favorite-character": "R2D2"
}

post_respons_values = requests.post("http://10.0.0.24:5000/starwars", json=data)
print(post_respons_values.text)