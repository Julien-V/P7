#!/usr/bin/python3
# coding : utf-8

from grandpy.api import api


class GMaps_API(api.GetAPI):
    def __init__(self, url, param, query):
        self.query = query
        self.param = param
        self.param['input'] = self.query
        super().__init__(url, param)

    def run(self):
        response = self.get_and_load()
        if "candidates" in response.keys():
            if len(response['candidates']):
                return response['candidates'][0]
        else:
            return None
