#!/usr/bin/python3
# coding : utf-8

import json
import requests


class GetAPI(object):
    """Base Class for all *_API class
        Send a request to url with a dict of param
    :return: json response in a dict
    """
    def __init__(self, url, param):
        """This method initializes the class
        :param url: url for the request
        :param param: params for request.get(), arguments to pass in url
        """
        self.url = url
        self.param = param
        self.headers = {'user-agent': 'OC_P7_GrandPy/0.1'}
        pass

    def get_and_load(self):
        """This method does the request and decode returned JSON
        :return: JSON decoded by json.loads()"""
        failstack = 0
        requesting = True
        while requesting and failstack <= 3:
            try:
                r = requests.get(
                    self.url,
                    headers=self.headers,
                    params=self.param)
                requesting = False
            except requests.exceptions.Timeout:
                print("[!] Timeout.")
                failstack += 1
            except requests.exceptions.RequestException as e:
                print(f"[!] Error : {e}")
                failstack += 1
        # if requesting, failstack > 3
        # so r.text do
        if not requesting:
            result = json.loads(r.text)
        else:
            result = dict()
        return result
