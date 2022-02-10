import json
from json.tool import main
from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PAYMENT_APP'


@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template('pay.html')

if __name__ == '__main__':
    app.run(debug=True)