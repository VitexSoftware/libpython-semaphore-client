# semaphore_client.ProjectsApi

All URIs are relative to *https://demo.ansible-semaphore.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_get**](ProjectsApi.md#projects_get) | **GET** /projects | Get projects
[**projects_post**](ProjectsApi.md#projects_post) | **POST** /projects | Create a new project


# **projects_get**
> [Project] projects_get()

Get projects

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import projects_api
from semaphore_client.model.project import Project
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ansible-semaphore.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_client.Configuration(
    host = "https://demo.ansible-semaphore.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearer
configuration.api_key['bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get projects
        api_response = api_instance.projects_get()
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling ProjectsApi->projects_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Project]**](Project.md)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of projects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_post**
> projects_post(project)

Create a new project

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import projects_api
from semaphore_client.model.project_request import ProjectRequest
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ansible-semaphore.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_client.Configuration(
    host = "https://demo.ansible-semaphore.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearer
configuration.api_key['bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project = ProjectRequest(
        name="Test",
        alert=True,
    ) # ProjectRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new project
        api_instance.projects_post(project)
    except semaphore_client.ApiException as e:
        print("Exception when calling ProjectsApi->projects_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**ProjectRequest**](ProjectRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

