#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import machine.sort as ana

# Flask configuration
DEBUG = True

# Create our app
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('default.html')

@app.route('/tab', methods=['POST'])
def sortTable():
    req = request.get_json()
    data = req.get('data', None)
    coeff = ana.analyseTab(data)

    if type(data) == list and data:
        resp = sorted(data)

        return "{'data_sorted': resp, 'coeff': str(coeff)}"

    return "{'error': 'Data sent is not List type or void'}"


app.run(host='0.0.0.0')
