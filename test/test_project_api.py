"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.8.34
    Generated by: https://openapi-generator.tech
"""


import unittest

import semaphore_client
from semaphore_client.api.project_api import ProjectApi  # noqa: E501


class TestProjectApi(unittest.TestCase):
    """ProjectApi unit test stubs"""

    def setUp(self):
        self.api = ProjectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_project_project_id_delete(self):
        """Test case for project_project_id_delete

        Delete project  # noqa: E501
        """
        pass

    def test_project_project_id_environment_environment_id_delete(self):
        """Test case for project_project_id_environment_environment_id_delete

        Removes environment  # noqa: E501
        """
        pass

    def test_project_project_id_environment_environment_id_put(self):
        """Test case for project_project_id_environment_environment_id_put

        Update environment  # noqa: E501
        """
        pass

    def test_project_project_id_environment_get(self):
        """Test case for project_project_id_environment_get

        Get environment  # noqa: E501
        """
        pass

    def test_project_project_id_environment_post(self):
        """Test case for project_project_id_environment_post

        Add environment  # noqa: E501
        """
        pass

    def test_project_project_id_events_get(self):
        """Test case for project_project_id_events_get

        Get Events related to this project  # noqa: E501
        """
        pass

    def test_project_project_id_get(self):
        """Test case for project_project_id_get

        Fetch project  # noqa: E501
        """
        pass

    def test_project_project_id_inventory_get(self):
        """Test case for project_project_id_inventory_get

        Get inventory  # noqa: E501
        """
        pass

    def test_project_project_id_inventory_inventory_id_delete(self):
        """Test case for project_project_id_inventory_inventory_id_delete

        Removes inventory  # noqa: E501
        """
        pass

    def test_project_project_id_inventory_inventory_id_put(self):
        """Test case for project_project_id_inventory_inventory_id_put

        Updates inventory  # noqa: E501
        """
        pass

    def test_project_project_id_inventory_post(self):
        """Test case for project_project_id_inventory_post

        create inventory  # noqa: E501
        """
        pass

    def test_project_project_id_keys_get(self):
        """Test case for project_project_id_keys_get

        Get access keys linked to project  # noqa: E501
        """
        pass

    def test_project_project_id_keys_key_id_delete(self):
        """Test case for project_project_id_keys_key_id_delete

        Removes access key  # noqa: E501
        """
        pass

    def test_project_project_id_keys_key_id_put(self):
        """Test case for project_project_id_keys_key_id_put

        Updates access key  # noqa: E501
        """
        pass

    def test_project_project_id_keys_post(self):
        """Test case for project_project_id_keys_post

        Add access key  # noqa: E501
        """
        pass

    def test_project_project_id_put(self):
        """Test case for project_project_id_put

        Update project  # noqa: E501
        """
        pass

    def test_project_project_id_repositories_get(self):
        """Test case for project_project_id_repositories_get

        Get repositories  # noqa: E501
        """
        pass

    def test_project_project_id_repositories_post(self):
        """Test case for project_project_id_repositories_post

        Add repository  # noqa: E501
        """
        pass

    def test_project_project_id_repositories_repository_id_delete(self):
        """Test case for project_project_id_repositories_repository_id_delete

        Removes repository  # noqa: E501
        """
        pass

    def test_project_project_id_tasks_get(self):
        """Test case for project_project_id_tasks_get

        Get Tasks related to current project  # noqa: E501
        """
        pass

    def test_project_project_id_tasks_last_get(self):
        """Test case for project_project_id_tasks_last_get

        Get last 200 Tasks related to current project  # noqa: E501
        """
        pass

    def test_project_project_id_tasks_post(self):
        """Test case for project_project_id_tasks_post

        Starts a job  # noqa: E501
        """
        pass

    def test_project_project_id_tasks_task_id_delete(self):
        """Test case for project_project_id_tasks_task_id_delete

        Deletes task (including output)  # noqa: E501
        """
        pass

    def test_project_project_id_tasks_task_id_get(self):
        """Test case for project_project_id_tasks_task_id_get

        Get a single task  # noqa: E501
        """
        pass

    def test_project_project_id_tasks_task_id_output_get(self):
        """Test case for project_project_id_tasks_task_id_output_get

        Get task output  # noqa: E501
        """
        pass

    def test_project_project_id_templates_get(self):
        """Test case for project_project_id_templates_get

        Get template  # noqa: E501
        """
        pass

    def test_project_project_id_templates_post(self):
        """Test case for project_project_id_templates_post

        create template  # noqa: E501
        """
        pass

    def test_project_project_id_templates_template_id_delete(self):
        """Test case for project_project_id_templates_template_id_delete

        Removes template  # noqa: E501
        """
        pass

    def test_project_project_id_templates_template_id_get(self):
        """Test case for project_project_id_templates_template_id_get

        Get template  # noqa: E501
        """
        pass

    def test_project_project_id_templates_template_id_put(self):
        """Test case for project_project_id_templates_template_id_put

        Updates template  # noqa: E501
        """
        pass

    def test_project_project_id_users_get(self):
        """Test case for project_project_id_users_get

        Get users linked to project  # noqa: E501
        """
        pass

    def test_project_project_id_users_post(self):
        """Test case for project_project_id_users_post

        Link user to project  # noqa: E501
        """
        pass

    def test_project_project_id_users_user_id_admin_delete(self):
        """Test case for project_project_id_users_user_id_admin_delete

        Revoke admin privileges  # noqa: E501
        """
        pass

    def test_project_project_id_users_user_id_admin_post(self):
        """Test case for project_project_id_users_user_id_admin_post

        Makes user admin  # noqa: E501
        """
        pass

    def test_project_project_id_users_user_id_delete(self):
        """Test case for project_project_id_users_user_id_delete

        Removes user from project  # noqa: E501
        """
        pass

    def test_project_project_id_views_get(self):
        """Test case for project_project_id_views_get

        Get view  # noqa: E501
        """
        pass

    def test_project_project_id_views_post(self):
        """Test case for project_project_id_views_post

        create view  # noqa: E501
        """
        pass

    def test_project_project_id_views_view_id_delete(self):
        """Test case for project_project_id_views_view_id_delete

        Removes view  # noqa: E501
        """
        pass

    def test_project_project_id_views_view_id_get(self):
        """Test case for project_project_id_views_view_id_get

        Get view  # noqa: E501
        """
        pass

    def test_project_project_id_views_view_id_put(self):
        """Test case for project_project_id_views_view_id_put

        Updates view  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
