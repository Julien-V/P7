#!/usr/bin/python3
# coding : utf-8

import json
import requests


class GetAPI(object):
    """Base Class for all *_API class"""
    def __init__(self, url, param):
        """This method initializes the class
        :param param: url arguments for the request
        :param db: database object
        :param cat_id: categorie id in table Categories
        """
        self.url = url
        self.param = param
        self.headers = {'user-agent': 'OC_P7_GrandPy/0.1'}
        pass

    def get_and_load(self):
        """This method does the request and decode returned JSON
        :return: JSON decoded by json.loads()"""
        requesting = True
        while requesting:
            try:
                r = requests.get(
                    self.url,
                    headers=self.headers,
                    params=self.param)
                requesting = False
            except requests.exceptions.Timeout:
                print("[!] Timeout.")
            except requests.exceptions.RequestException as e:
                print(f"[!] Error : {e}")
        result = json.loads(r.text)
        return result
