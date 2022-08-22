
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from semaphore_client.api.authentication_api import AuthenticationApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from semaphore.authentication_api import AuthenticationApi
from semaphore.default_api import DefaultApi
from semaphore.project_api import ProjectApi
from semaphore.projects_api import ProjectsApi
from semaphore.schedule_api import ScheduleApi
from semaphore.user_api import UserApi
