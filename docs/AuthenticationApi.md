# semaphore_client.AuthenticationApi

All URIs are relative to *https://demo.ansible-semaphore.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login_post**](AuthenticationApi.md#auth_login_post) | **POST** /auth/login | Performs Login
[**auth_logout_post**](AuthenticationApi.md#auth_logout_post) | **POST** /auth/logout | Destroys current session
[**user_tokens_api_token_id_delete**](AuthenticationApi.md#user_tokens_api_token_id_delete) | **DELETE** /user/tokens/{api_token_id} | Expires API token
[**user_tokens_get**](AuthenticationApi.md#user_tokens_get) | **GET** /user/tokens | Fetch API tokens for user
[**user_tokens_post**](AuthenticationApi.md#user_tokens_post) | **POST** /user/tokens | Create an API token


# **auth_login_post**
> auth_login_post(login_body)

Performs Login

Upon success you will be logged in

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import authentication_api
from semaphore_client.model.login import Login
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
    api_instance = authentication_api.AuthenticationApi(api_client)
    login_body = Login(
        auth="auth_example",
        password="password_example",
    ) # Login | 

    # example passing only required values which don't have defaults set
    try:
        # Performs Login
        api_instance.auth_login_post(login_body)
    except semaphore_client.ApiException as e:
        print("Exception when calling AuthenticationApi->auth_login_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_body** | [**Login**](Login.md)|  |

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
**204** | You are logged in |  -  |
**400** | something in body is missing / is invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_logout_post**
> auth_logout_post()

Destroys current session

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import authentication_api
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
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Destroys current session
        api_instance.auth_logout_post()
    except semaphore_client.ApiException as e:
        print("Exception when calling AuthenticationApi->auth_logout_post: %s\n" % e)
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
**204** | Your session was successfully nuked |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tokens_api_token_id_delete**
> user_tokens_api_token_id_delete(api_token_id)

Expires API token

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import authentication_api
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
    api_instance = authentication_api.AuthenticationApi(api_client)
    api_token_id = "kwofd61g93-yuqvex8efmhjkgnbxlo8mp1tin6spyhu=" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Expires API token
        api_instance.user_tokens_api_token_id_delete(api_token_id)
    except semaphore_client.ApiException as e:
        print("Exception when calling AuthenticationApi->user_tokens_api_token_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token_id** | **str**|  |

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
**204** | Expired API Token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tokens_get**
> [APIToken] user_tokens_get()

Fetch API tokens for user

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import authentication_api
from semaphore_client.model.api_token import APIToken
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
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch API tokens for user
        api_response = api_instance.user_tokens_get()
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling AuthenticationApi->user_tokens_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[APIToken]**](APIToken.md)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API Tokens |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tokens_post**
> APIToken user_tokens_post()

Create an API token

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import authentication_api
from semaphore_client.model.api_token import APIToken
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
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create an API token
        api_response = api_instance.user_tokens_post()
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling AuthenticationApi->user_tokens_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**APIToken**](APIToken.md)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | API Token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

