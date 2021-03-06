#!/usr/bin/python3
# coding : utf-8

from grandpy.parser import GrandPy


class TestGrandPy:
    TO_PARSE = (
        "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
    PARSER = GrandPy()
    RESULT_API = {
        'p_query': 'connais openclassrooms',
        'map': {'formatted_address': 'address_oc'}
    }
    RESULT_API_NONE = {
        'p_query': 'connais openclassrooms',
        'map': None
    }

    def test_import_stop_words(self):
        """This method tests stop words importation"""
        assert (isinstance(self.PARSER.stop_words, list))

    def test_parse(self):
        """This method uses GrandPy.parse() to parse TO_PARSE"""
        PARSED = self.PARSER.parse(self.TO_PARSE)
        assert (PARSED == "openclassrooms")

    def test_think(self):
        """This method tests GrandPy.think() with RESULT_API"""
        RESULT = self.PARSER.think(self.RESULT_API)
        gp_response = RESULT['gp']
        f_address = self.RESULT_API['map']['formatted_address']
        assert (f_address in gp_response)

    def test_think_none(self):
        """This method tests GrandPy.think() with RESULT_API_NONE"""
        RESULT = self.PARSER.think(self.RESULT_API_NONE)
        gp_response = RESULT['gp']
        p_query = self.RESULT_API['p_query']
        assert (p_query in gp_response)
