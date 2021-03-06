# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from apps.views.views import HelloWorld, SortTable


# Flask configuration
DEBUG = True

# Create our app
app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)


api.add_resource(HelloWorld, '/')
api.add_resource(SortTable, '/tab')
