#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 01:46:49 2019

@author: aishwary
"""
from flask import Flask, request,jsonify,render_template

from flask_restful import Resource, Api
import sys

sys.path.append('/home/aishwary/PycharmProjects/chatbot/chatbot.py')
from chatbot import tutbot







app = Flask(__name__)

api = Api(app)

#@app.route('/')
#def from_example():

#return '''<form method="POST">
#inputlocation: <input type="text" name="language"><br>
#outputlocation: <input type="text" name="framework"><br>
#predicter_type:<input type="text" name="predicter_type"><br>
#feature_dim:<input type="integer" name="feature_dim">
#</form>'''

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/get") #GET requests will be blocked

def json_example():

    userText = request.args.get('msg')

    ans=str(tutbot(userText))

    return ans


if __name__ == "__main__":
    app.run(debug=True,port=7778)
