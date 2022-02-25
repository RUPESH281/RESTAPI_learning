import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/signUpNew')
def signUpNew():
  base_url = requests.post("https://erp-test.fooddarzee.com/docs/api-docs.json")
  data= base_url.json()
  for key in data:
    if key=='paths':
        data1=data[key]
        for value in data1:
            if value=='/signUpNew':
                data2=data1[value]
                return jsonify({"message":data2})

@app.route('/login')
def login():
  base_url = requests.post("https://erp-test.fooddarzee.com/docs/api-docs.json")
  data= base_url.json()
  for key in data:
    if key=='paths':
        data1=data[key]
        for value in data1:
            if value=='/login':
                data2=data1[value]
                return jsonify({"message":data2})

@app.route('/resendOtp')
def resendOtp():
  base_url = requests.post("https://erp-test.fooddarzee.com/docs/api-docs.json")
  data= base_url.json()
  for key in data:
    if key=='paths':
        data1=data[key]
        for value in data1:
            if value=='/resendOtp':
                data2=data1[value]
                return jsonify({"message":data2})

@app.route('/verifyOtp')
def verifyOtp():
  base_url = requests.post("https://erp-test.fooddarzee.com/docs/api-docs.json")
  data= base_url.json()
  for key in data:
    if key=='paths':
        data1=data[key]
        for value in data1:
            if value=='/verifyOtp':
                data2=data1[value]
                return jsonify({"message":data2})

@app.route('/v1/address')
def v1_address():
  base_url = requests.get("https://erp-test.fooddarzee.com/docs/api-docs.json")
  data= base_url.json()
  for key in data:
    if key=='paths':
        data1=data[key]
        for value in data1:
            if value=='/v1/address':
                data2=data1[value]
                return jsonify({"message":data2})

if __name__ == '__main__':
    app.run(debug=True)