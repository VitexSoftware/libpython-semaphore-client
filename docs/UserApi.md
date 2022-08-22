# semaphore_client.UserApi

All URIs are relative to *https://demo.ansible-semaphore.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_get**](UserApi.md#user_get) | **GET** /user/ | Fetch logged in user
[**user_tokens_api_token_id_delete**](UserApi.md#user_tokens_api_token_id_delete) | **DELETE** /user/tokens/{api_token_id} | Expires API token
[**user_tokens_get**](UserApi.md#user_tokens_get) | **GET** /user/tokens | Fetch API tokens for user
[**user_tokens_post**](UserApi.md#user_tokens_post) | **POST** /user/tokens | Create an API token
[**users_get**](UserApi.md#users_get) | **GET** /users | Fetches all users
[**users_post**](UserApi.md#users_post) | **POST** /users | Creates a user
[**users_user_id_delete**](UserApi.md#users_user_id_delete) | **DELETE** /users/{user_id}/ | Deletes user
[**users_user_id_get**](UserApi.md#users_user_id_get) | **GET** /users/{user_id}/ | Fetches a user profile
[**users_user_id_password_post**](UserApi.md#users_user_id_password_post) | **POST** /users/{user_id}/password | Updates user password
[**users_user_id_put**](UserApi.md#users_user_id_put) | **PUT** /users/{user_id}/ | Updates user details


# **user_get**
> User user_get()

Fetch logged in user

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import user_api
from semaphore_client.model.user import User
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch logged in user
        api_response = api_instance.user_get()
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling UserApi->user_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User |  -  |

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
from semaphore import user_api
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
    api_instance = user_api.UserApi(api_client)
    api_token_id = "kwofd61g93-yuqvex8efmhjkgnbxlo8mp1tin6spyhu=" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Expires API token
        api_instance.user_tokens_api_token_id_delete(api_token_id)
    except semaphore_client.ApiException as e:
        print("Exception when calling UserApi->user_tokens_api_token_id_delete: %s\n" % e)
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
from semaphore import user_api
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch API tokens for user
        api_response = api_instance.user_tokens_get()
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling UserApi->user_tokens_get: %s\n" % e)
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
from semaphore import user_api
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create an API token
        api_response = api_instance.user_tokens_post()
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling UserApi->user_tokens_post: %s\n" % e)
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

# **users_get**
> [User] users_get()

Fetches all users

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import user_api
from semaphore_client.model.user import User
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetches all users
        api_response = api_instance.users_get()
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling UserApi->users_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[User]**](User.md)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> User users_post(user)

Creates a user

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import user_api
from semaphore_client.model.user_request import UserRequest
from semaphore_client.model.user import User
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
    api_instance = user_api.UserApi(api_client)
    user = UserRequest(
        name="Integration Test User",
        username="test-user",
        email="test@ansiblesemaphore.test",
        alert=True,
        admin=True,
    ) # UserRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a user
        api_response = api_instance.users_post(user)
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling UserApi->users_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UserRequest**](UserRequest.md)|  |

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain; charset=utf-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User created |  -  |
**400** | User creation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_delete**
> users_user_id_delete(user_id)

Deletes user

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import user_api
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
    api_instance = user_api.UserApi(api_client)
    user_id = 2 # int | User ID

    # example passing only required values which don't have defaults set
    try:
        # Deletes user
        api_instance.users_user_id_delete(user_id)
    except semaphore_client.ApiException as e:
        print("Exception when calling UserApi->users_user_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID |

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
**204** | User deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_get**
> User users_user_id_get(user_id)

Fetches a user profile

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import user_api
from semaphore_client.model.user import User
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
    api_instance = user_api.UserApi(api_client)
    user_id = 2 # int | User ID

    # example passing only required values which don't have defaults set
    try:
        # Fetches a user profile
        api_response = api_instance.users_user_id_get(user_id)
        pprint(api_response)
    except semaphore_client.ApiException as e:
        print("Exception when calling UserApi->users_user_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID |

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer), [cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User profile |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_password_post**
> users_user_id_password_post(user_id, password)

Updates user password

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import user_api
from semaphore_client.model.users_user_id_password_post_request import UsersUserIdPasswordPostRequest
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
    api_instance = user_api.UserApi(api_client)
    user_id = 2 # int | User ID
    password = UsersUserIdPasswordPostRequest(
        password="password_example",
    ) # UsersUserIdPasswordPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Updates user password
        api_instance.users_user_id_password_post(user_id, password)
    except semaphore_client.ApiException as e:
        print("Exception when calling UserApi->users_user_id_password_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID |
 **password** | [**UsersUserIdPasswordPostRequest**](UsersUserIdPasswordPostRequest.md)|  |

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
**204** | Password updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_put**
> users_user_id_put(user_id, user)

Updates user details

### Example

* Api Key Authentication (bearer):
* Api Key Authentication (cookie):

```python
import time
import semaphore_client
from semaphore import user_api
from semaphore_client.model.user_put_request import UserPutRequest
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
    api_instance = user_api.UserApi(api_client)
    user_id = 2 # int | User ID
    user = UserPutRequest(
        name="Integration Test User2",
        username="test-user2",
        email="test2@ansiblesemaphore.test",
        alert=True,
        admin=True,
    ) # UserPutRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Updates user details
        api_instance.users_user_id_put(user_id, user)
    except semaphore_client.ApiException as e:
        print("Exception when calling UserApi->users_user_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID |
 **user** | [**UserPutRequest**](UserPutRequest.md)|  |

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
**204** | User Updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

