#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint
from flask import request
from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class SortTable(Resource):
    def post(self):

        req = request.get_json()
        data = req.get('data', None)

        if type(data) == list and data:
            resp = sorted(data)

            return {'data_sorted': resp}

        return {'error': 'Data sent is not List type or void'}
