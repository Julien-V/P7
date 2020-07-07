#!/usr/bin/python3
# coding : utf-8

import json
import string


class GrandPy(object):
    """This class parse a query and return a response"""
    def __init__(self):
        """This method initialize the class"""
        # https://github.com/6/stopwords-json
        with open("grandpy/static/fr.json") as file_a:
            self.stop_words = json.loads(file_a.read())
        # add some greetings to self.stop_words
        greetings = 'bonjour hey salut hello'
        self.stop_words += greetings.split()
        # add more words to self.stop_words
        words = "grandpy connais adresse situe"
        self.stop_words += words.split()
        # add punctuation to self.stop_words
        self.punctuation = "c' d' j' l' m' n' s' t' u' y'".split()
        self.punctuation += list(string.punctuation)

    def parse(self, query):
        query = query.lower()
        # remove punctuation
        for elem in self.punctuation:
            if elem in query:
                query = query.replace(elem, ' ')
        # remove stop words
        parsed_query = list()
        for word in query.split():
            if word not in self.stop_words:
                parsed_query.append(word)
        # rewrite parsed_query into str with space :
        parsed_query = ''.join(f'{x} ' for x in parsed_query)
        # return parsed query without final space
        return parsed_query[:-1]

    def think(self, result):
        """This method formats the result in a
        text that will be displayed (grandpy's responses)
        :param result: dict, with "map" key
        :return: result dict with a new key "gp"
        """
        result['gp'] = None
        if result['map'] is None:
            gp_response = "Ça ne me dit rien du tout !"
            gp_response += f" Que veut dire {result['p_query']} ?"
        else:
            gp_response = "Bien sûr que je connais cette adresse !"
            gp_response += " Je ne suis quand même pas si vieux : "
            gp_response += str(result['map']['formatted_address'])
        result['gp'] = gp_response
        return result
