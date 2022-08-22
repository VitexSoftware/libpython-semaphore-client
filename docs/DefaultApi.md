# semaphore_client.DefaultApi

All URIs are relative to *https://demo.ansible-semaphore.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_get**](DefaultApi.md#events_get) | **GET** /events | Get Events related to Semaphore and projects you are part of
[**events_last_get**](DefaultApi.md#events_last_get) | **GET** /events/last | Get last 200 Events related to Semaphore and projects you are part of
[**info_get**](DefaultApi.md#info_get) | **GET** /info | Fetches information about semaphore
[**ping_get**](DefaultApi.md#ping_get) | **GET** /ping | PING test
[**ws_get**](DefaultApi.md#ws_get) | **GET** /ws | Websocket handler


# **events_get**
> [Event] events_get()

Get Events related to Semaphore and projects you are part of

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import default_api
from semaphore_client.model.event import Event
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Events related to Semaphore and projects you are part of
        api_response = api_instance.events_get()
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling DefaultApi->events_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Event]**](Event.md)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of events in chronological order |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_last_get**
> [Event] events_last_get()

Get last 200 Events related to Semaphore and projects you are part of

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import default_api
from semaphore_client.model.event import Event
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get last 200 Events related to Semaphore and projects you are part of
        api_response = api_instance.events_last_get()
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling DefaultApi->events_last_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Event]**](Event.md)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of events in chronological order |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_get**
> InfoType info_get()

Fetches information about semaphore

you must be authenticated to use this

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import default_api
from semaphore_client.model.info_type import InfoType
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetches information about semaphore
        api_response = api_instance.info_get()
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling DefaultApi->info_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InfoType**](InfoType.md)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_get**
> str ping_get()

PING test

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import default_api
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # PING test
        api_response = api_instance.ping_get()
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling DefaultApi->ping_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful \&quot;PONG\&quot; reply |  * content-type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ws_get**
> ws_get()

Websocket handler

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import default_api
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Websocket handler
        api_instance.ws_get()
    except semaphore_client.ApiException as e:
        print("Exception when calling DefaultApi->ws_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | OK |  -  |
**401** | not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

