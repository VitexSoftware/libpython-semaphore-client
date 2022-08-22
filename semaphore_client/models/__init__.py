# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from semaphore_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from semaphore_client.model.api_token import APIToken
from semaphore_client.model.access_key import AccessKey
from semaphore_client.model.access_key_request import AccessKeyRequest
from semaphore_client.model.environment import Environment
from semaphore_client.model.environment_request import EnvironmentRequest
from semaphore_client.model.event import Event
from semaphore_client.model.info_type import InfoType
from semaphore_client.model.info_type_update import InfoTypeUpdate
from semaphore_client.model.inventory import Inventory
from semaphore_client.model.inventory_request import InventoryRequest
from semaphore_client.model.login import Login
from semaphore_client.model.project import Project
from semaphore_client.model.project_project_id_delete_request import ProjectProjectIdDeleteRequest
from semaphore_client.model.project_project_id_tasks_get_request import ProjectProjectIdTasksGetRequest
from semaphore_client.model.project_project_id_users_get_request import ProjectProjectIdUsersGetRequest
from semaphore_client.model.project_request import ProjectRequest
from semaphore_client.model.repository import Repository
from semaphore_client.model.repository_request import RepositoryRequest
from semaphore_client.model.schedule import Schedule
from semaphore_client.model.schedule_request import ScheduleRequest
from semaphore_client.model.task import Task
from semaphore_client.model.task_output import TaskOutput
from semaphore_client.model.template import Template
from semaphore_client.model.template_request import TemplateRequest
from semaphore_client.model.user import User
from semaphore_client.model.user_put_request import UserPutRequest
from semaphore_client.model.user_request import UserRequest
from semaphore_client.model.users_user_id_password_post_request import UsersUserIdPasswordPostRequest
from semaphore_client.model.view import View
from semaphore_client.model.view_request import ViewRequest
