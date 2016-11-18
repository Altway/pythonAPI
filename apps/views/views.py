#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource
import apps.machine.sort as ana

class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}

class SortTable(Resource):
    def post(self):

        req = request.get_json()
        data = req.get('data', None)
        #coeff = ana.linearAnalyseTab(data)
        coeff = ana.polynomialAnalyseTab(data)

        if type(data) == list and data:
            resp = sorted(data)

            return {"data_sorted": resp, "coeff": str(coeff)}

        return {"error": "Data sent is not List type or void"}
