"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.8.34
    Generated by: https://openapi-generator.tech
"""


import unittest

import semaphore_client
from semaphore_client.api.authentication_api import AuthenticationApi  # noqa: E501


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_auth_login_post(self):
        """Test case for auth_login_post

        Performs Login  # noqa: E501
        """
        pass

    def test_auth_logout_post(self):
        """Test case for auth_logout_post

        Destroys current session  # noqa: E501
        """
        pass

    def test_user_tokens_api_token_id_delete(self):
        """Test case for user_tokens_api_token_id_delete

        Expires API token  # noqa: E501
        """
        pass

    def test_user_tokens_get(self):
        """Test case for user_tokens_get

        Fetch API tokens for user  # noqa: E501
        """
        pass

    def test_user_tokens_post(self):
        """Test case for user_tokens_post

        Create an API token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
