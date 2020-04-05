#!flask/bin/python
from flask import Flask, request

app = Flask(__name__)

@app.route("/ziyotek", methods=['GET'])
def index():
    return "Hello World"

@app.route("/starwars", methods=['POST'])
def postmethod():
    data = request.get_json()
    print("This is JSON")
    print(data)
    return "THIS IS DATA!!!" + data["favorite-character"]


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
