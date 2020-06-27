#!/usr/bin/python3
# coding : utf-8

import os
import json

from grandpy.api.maps_api import GMaps_API


def j(json_file):
    path = os.path.join("test/samples/", json_file)
    with open(path, "r") as file_a:
        json_file = file_a.read()
    return json.loads(json_file)


class MockResponse:
    @staticmethod
    def get_valid():
        return j("valid_g_maps.json")

    @staticmethod
    def get_invalid():
        return j("invalid_g_maps.json")

    @staticmethod
    def get_no_candidates():
        return j("no_candidates_g_maps.json")


class TestGMaps_API:
    g_maps = GMaps_API("http://maps.etc", {'param': "test"}, "query")

    def test_run_valid(self, monkeypatch):
        def mock_get_and_load(*args):
            return MockResponse.get_valid()

        monkeypatch.setattr(GMaps_API, "get_and_load", mock_get_and_load)
        result = self.g_maps.run()
        assert (result['formatted_address'])

    def test_run_invalid(self, monkeypatch):
        def mock_get_and_load(*args):
            return MockResponse.get_invalid()

        monkeypatch.setattr(GMaps_API, "get_and_load", mock_get_and_load)
        result = self.g_maps.run()
        assert (result is None)

    def test_run_no_candidates(self, monkeypatch):
        def mock_get_and_load(*args):
            return MockResponse.get_no_candidates()

        monkeypatch.setattr(GMaps_API, "get_and_load", mock_get_and_load)
        result = self.g_maps.run()
        assert (result is None)
