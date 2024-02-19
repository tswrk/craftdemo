from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

#Health route
@app.route('/health')
def health():
    return jsonify({'status': 'ok'})

#Diag check route
@app.route('/diag')
def diag():
    url = 'https://www.travel-advisory.info/api'
    response = requests.get(url)
    return jsonify(response.json()['api_status'])

#Convert route
@app.route('/convert/<country_name>')
def convert_country(country_name):
    url = "https://www.travel-advisory.info/api"
    response = requests.get(url)
    data = response.json()
    
    for code, info in data["data"].items():
        if info["name"] == country_name:
            return jsonify({"country_code": code})

if __name__ == '__main__':
    app.run(debug=True)
