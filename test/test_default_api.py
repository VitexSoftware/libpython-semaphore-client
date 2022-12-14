"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.8.34
    Generated by: https://openapi-generator.tech
"""


import unittest

import semaphore_client
from semaphore_client.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_events_get(self):
        """Test case for events_get

        Get Events related to Semaphore and projects you are part of  # noqa: E501
        """
        pass

    def test_events_last_get(self):
        """Test case for events_last_get

        Get last 200 Events related to Semaphore and projects you are part of  # noqa: E501
        """
        pass

    def test_info_get(self):
        """Test case for info_get

        Fetches information about semaphore  # noqa: E501
        """
        pass

    def test_ping_get(self):
        """Test case for ping_get

        PING test  # noqa: E501
        """
        pass

    def test_ws_get(self):
        """Test case for ws_get

        Websocket handler  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
