#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
