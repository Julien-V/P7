#!/usr/bin/python3
# coding : utf-8


class Config(object):
    DEBUG = False
    TESTING = False
    APP_TITLE = "GrandPyBot"
    APP_AUTHOR = "Julien-V"
    GITHUB_LINK = "https://github.com/Julien-V/P7"
    G_API_URL = (
        "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?")
    G_API_PARAMS = {
        'inputtype': 'textquery',
        'input': "",
        'language': 'fr',
        'fields': "formatted_address,name,geometry",
    }
    W_API_URL = (
        "https://fr.wikipedia.org/w/api.php")
    W_API_PARAMS = {
        "action": "query",
        "format": "json",
        "redirects": 1,
        "utf8": "",
        "prop": "extracts",
        "exintro": "",
        "explaintext": "",
        "titles": ""
    }
    W_URL_PAGE_ID = (
        "http://fr.wikipedia.org/?curid=")


class DevelopmentConfig(Config):
    DEBUG = True
