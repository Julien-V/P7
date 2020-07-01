#!/usr/bin/python3
# coding : utf-8

from grandpy.api import api


class Wikipedia_API(api.GetAPI):
    def __init__(self, url, param, query, p_query):
        self.query = query
        self.param = param
        self.param["titles"] = self.query
        self.p_query = p_query
        super().__init__(url, param)

    def process(self, response):
        try:
            pages_dict = response['query']['pages']
        except KeyError:
            return None
        first_key = next(iter(pages_dict))
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
        response = self.get_and_load()
        output = self.process(response)
        if output is not None:
            return output
        else:
            self.param['titles'] = self.p_query
            response = self.get_and_load()
            output = self.process(response)
            return output
