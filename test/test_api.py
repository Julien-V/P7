#!/usr/bin/python3
# coding : utf-8

import os
import json
import pytest

from grandpy.api.api import GetAPI
from grandpy.api.maps_api import GMaps_API
from grandpy.api.wiki_api import Wikipedia_API


def j(json_file):
    path = os.path.join("test/samples/", json_file)
    with open(path, "r") as file_a:
        json_file = file_a.read()
    return json.loads(json_file)


@pytest.fixture
def patch_get_and_load(monkeypatch):
    def mock_get_and_load(*args):
        return json_file.values
    monkeypatch.setattr(GetAPI, "get_and_load", mock_get_and_load)

    class FakeJSON_file:
        pass

    json_file = FakeJSON_file()
    json_file.values = None
    return json_file


class TestGMaps_API:
    g_maps = GMaps_API("http://maps.etc", {'param': "test"}, "query")

    def test_run_valid(self, patch_get_and_load):
        patch_get_and_load.values = j("valid_g_maps.json")
        result = self.g_maps.run()
        assert (isinstance(result['formatted_address'], str))

    def test_run_invalid(self, patch_get_and_load):
        patch_get_and_load.values = j("invalid_g_maps.json")
        result = self.g_maps.run()
        assert (result is None)

    def test_run_no_candidates(self, patch_get_and_load):
        patch_get_and_load.values = j("unknown_g_maps.json")
        result = self.g_maps.run()
        assert (result is None)


class TestWikipedia_API:
    wiki = Wikipedia_API(
        "http://wikipedia.etc",
        {'param': "test"},
        "query",
        "p_query")

    def test_run_valid(self, patch_get_and_load):
        patch_get_and_load.values = j("valid_wiki.json")
        result = self.wiki.run()
        assert (isinstance(result, dict))

    def test_run_invalid(self, patch_get_and_load):
        # a test with a different json file
        # like valid_g_maps.json
        # result should be None
        patch_get_and_load.values = j("invalid_wiki.json")
        result = self.wiki.run()
        assert (result is None)

    def test_run_unknown(self, patch_get_and_load):
        patch_get_and_load.values = j("unknown_wiki.json")
        result = self.wiki.run()
        assert (result is None)
