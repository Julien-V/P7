#!/usr/bin/python3
# coding : utf-8

from grandpy.api import api


class Wikipedia_API(api.GetAPI):
    """An api.GetApi class with appropriate
    process of Wikipedia API's responses
    """
    def __init__(self, url, param, query, p_query):
        """This method initializes the class
        :param url: str, GMaps api url
        :param param: dict
        :param query: str, our search
        :param p_query: str, the original parsed query
        """
        self.query = query
        self.param = param
        self.param["titles"] = self.query
        self.p_query = p_query
        super().__init__(url, param)

    def process(self, response):
        """This method processes the API response
        :param response: dict
        :return: dict if an article is found
        :return: None for others situations
        """
        try:
            pages_dict = response['query']['pages']
        except KeyError:
            # invalid API response
            return None
        first_key = next(iter(pages_dict))
        # if we have a result
        if first_key != "-1":
            page = pages_dict[first_key]
            output = dict()
            output['page_id'] = page['pageid']
            output['title'] = page['title']
            output['extract'] = page['extract']
            if len(output['extract']) > 500:
                output['extract'] = output['extract'][:500]+" ..."
            return output
        else:
            return None

    def run(self):
        """This method calls api.GetAPI.get_and_load method,
        grab response (a dict) and call process() to process it
        return a dict if the response is the response requested
        is the one requested, else retry the search with self.p_query
        and return the result of process() (dict|None)
        :return: a dict of a wikipedia page
        :return: None if unknown response
        """
        response = self.get_and_load()
        output = self.process(response)
        if output is not None:
            return output
        else:
            self.param['titles'] = self.p_query
            response = self.get_and_load()
            output = self.process(response)
            return output
