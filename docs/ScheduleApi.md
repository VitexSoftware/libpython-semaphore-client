# semaphore_client.ScheduleApi

All URIs are relative to *https://demo.ansible-semaphore.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_project_id_schedules_post**](ScheduleApi.md#project_project_id_schedules_post) | **POST** /project/{project_id}/schedules | create schedule
[**project_project_id_schedules_schedule_id_delete**](ScheduleApi.md#project_project_id_schedules_schedule_id_delete) | **DELETE** /project/{project_id}/schedules/{schedule_id} | Deletes schedule
[**project_project_id_schedules_schedule_id_get**](ScheduleApi.md#project_project_id_schedules_schedule_id_get) | **GET** /project/{project_id}/schedules/{schedule_id} | Get schedule
[**project_project_id_schedules_schedule_id_put**](ScheduleApi.md#project_project_id_schedules_schedule_id_put) | **PUT** /project/{project_id}/schedules/{schedule_id} | Updates schedule


# **project_project_id_schedules_post**
> Schedule project_project_id_schedules_post(project_id, schedule)

create schedule

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import schedule_api
from semaphore_client.model.schedule_request import ScheduleRequest
from semaphore_client.model.schedule import Schedule
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
    api_instance = schedule_api.ScheduleApi(api_client)
    project_id = 1 # int | Project ID
    schedule = ScheduleRequest(
        id=1,
        cron_format="* * * 1 *",
        project_id=1,
        template_id=1,
    ) # ScheduleRequest | 

    # example passing only required values which don't have defaults set
    try:
        # create schedule
        api_response = api_instance.project_project_id_schedules_post(project_id, schedule)
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling ScheduleApi->project_project_id_schedules_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID |
 **schedule** | [**ScheduleRequest**](ScheduleRequest.md)|  |

### Return type

[**Schedule**](Schedule.md)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain; charset=utf-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | schedule created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_schedules_schedule_id_delete**
> project_project_id_schedules_schedule_id_delete(project_id, schedule_id)

Deletes schedule

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import schedule_api
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
    api_instance = schedule_api.ScheduleApi(api_client)
    project_id = 1 # int | Project ID
    schedule_id = 9 # int | schedule ID

    # example passing only required values which don't have defaults set
    try:
        # Deletes schedule
        api_instance.project_project_id_schedules_schedule_id_delete(project_id, schedule_id)
    except semaphore_client.ApiException as e:
        print("Exception when calling ScheduleApi->project_project_id_schedules_schedule_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID |
 **schedule_id** | **int**| schedule ID |

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | schedule deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_schedules_schedule_id_get**
> Schedule project_project_id_schedules_schedule_id_get(project_id, schedule_id)

Get schedule

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import schedule_api
from semaphore_client.model.schedule import Schedule
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
    api_instance = schedule_api.ScheduleApi(api_client)
    project_id = 1 # int | Project ID
    schedule_id = 9 # int | schedule ID

    # example passing only required values which don't have defaults set
    try:
        # Get schedule
        api_response = api_instance.project_project_id_schedules_schedule_id_get(project_id, schedule_id)
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling ScheduleApi->project_project_id_schedules_schedule_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID |
 **schedule_id** | **int**| schedule ID |

### Return type

[**Schedule**](Schedule.md)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Schedule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_schedules_schedule_id_put**
> project_project_id_schedules_schedule_id_put(project_id, schedule_id, schedule)

Updates schedule

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import schedule_api
from semaphore_client.model.schedule_request import ScheduleRequest
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
    api_instance = schedule_api.ScheduleApi(api_client)
    project_id = 1 # int | Project ID
    schedule_id = 9 # int | schedule ID
    schedule = ScheduleRequest(
        id=1,
        cron_format="* * * 1 *",
        project_id=1,
        template_id=1,
    ) # ScheduleRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Updates schedule
        api_instance.project_project_id_schedules_schedule_id_put(project_id, schedule_id, schedule)
    except semaphore_client.ApiException as e:
        print("Exception when calling ScheduleApi->project_project_id_schedules_schedule_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID |
 **schedule_id** | **int**| schedule ID |
 **schedule** | [**ScheduleRequest**](ScheduleRequest.md)|  |

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
**204** | schedule updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

