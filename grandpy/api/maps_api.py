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
        # we have one key 'candidates' in response dict
        # its value is a list of possible candidates
        # so let's select the first one ...
        # yep, i didn't read enough the doc
        # i learned it the hard way x)
        if len(response['candidates']):
            return response['candidates'][0]
        else:
            return None
