#!/usr/bin/python3
# coding : utf-8

from grandpy.api import api


class GMaps_API(api.GetAPI):
    """An api.GetApi class with appropriate
    process of Google Maps API's responses
    """
    def __init__(self, url, param, query):
        """This method initializes the class
        :param url: str, GMaps api url
        :param param: dict
        :param query: str, the parsed query
        """
        self.query = query
        self.param = param
        self.param['input'] = self.query
        super().__init__(url, param)

    def run(self):
        """This method calls api.GetAPI.get_and_load method,
        grab response (a dict) and return a dict if the response
        is the one requested, else return None
        :return: a dict of a candidate
        :return: None if unknown response
        """
        response = self.get_and_load()
        if "candidates" in response.keys():
            if len(response['candidates']):
                # return first candidate
                return response['candidates'][0]
        else:
            # No places found or response format invalid
            return None
