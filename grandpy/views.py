#!/usr/bin/python3
# coding : utf-8

import os

from flask import Flask, render_template
from flask import jsonify, request

from grandpy.parser import GrandPy
from grandpy.api.maps_api import GMaps_API
from grandpy.api.wiki_api import Wikipedia_API

# app creation and config
app = Flask(__name__)
app.config.from_object('config.Config')

is_prod = os.environ.get('IS_HEROKU', None)
if not is_prod:
    app.config.from_envvar('GRANDPY_SETTINGS')
else:
    app.config['MAPS_API_KEY'] = os.environ.get('MAPS_API_KEY', None)
app.config['G_API_PARAMS']["key"] = app.config['MAPS_API_KEY']

gp = GrandPy()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/ask", methods=["POST"])
def ask():
    query = request.form['content']
    p_query = gp.parse(query)
    result = {
        'query': query,
        'p_query': p_query,
    }
    # Google Maps Api
    gmaps_url, gmaps_params = (
        app.config['G_API_URL'],
        app.config['G_API_PARAMS'])
    map_api = GMaps_API(gmaps_url, gmaps_params, p_query)
    result['map'] = map_api.run()
    if result['map'] is not None:
        # Wiki Api
        wiki_url, wiki_params = (
            app.config['W_API_URL'],
            app.config['W_API_PARAMS'])
        wiki_api = Wikipedia_API(
            wiki_url,
            wiki_params,
            result['map']['name'],
            p_query)
        result['wiki'] = wiki_api.run()
        if result['wiki'] is not None:
            page_id = result['wiki']['page_id']
            url = app.config['W_URL_PAGE_ID'] + str(page_id)
            result['wiki']['url'] = url
    else:
        result['wiki'] = None
    result = gp.think(result)
    # to json and send
    json = jsonify(
        response=result['gp'],
        g_maps=result['map'],
        wiki=result['wiki'])
    return json
