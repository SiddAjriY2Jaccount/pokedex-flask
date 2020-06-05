from app import app
from flask import render_template, url_for
import requests
import json
import ast
import os

@app.route('/')
@app.route('/index')
def index():
    f = open("./static/cache/api-cache.txt", "r")
    pokedex_dict = ast.literal_eval(f.read())
    return render_template('index.html', pokedex = pokedex_dict)
