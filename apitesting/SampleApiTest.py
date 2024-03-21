import requests
from requests import HTTPError
import urllib3

#Session Usage
def test_get_request_session_usage():
        s = requests.session()

        #When using Python requests Session objects, you can
        # persist headers of requests being made within the session by providing data to the properties
        # of the session.

        s.headers.update({'accept':'datagy'})

        response = s.get('https://httpbin.org/headers')
        print(response.text)

        # It’s important to note that if we had passed headers into a method call
        # (rather than updating the session) the headers aren’t persisted across the session.

        #Prepared Requests

        #Whenever you receive a Response object from an API call or a Session call,
        # the request attribute is actually the PreparedRequest that was used.
        # In some cases you may wish to do some
        # extra work to the body or headers (or anything else really) before sending a request.

        user_id = 2
        url = f'https://reqres.in/api/users/{user_id}'
        print(url)
        requests_get = requests.get(url)

        requests_get_json = requests_get.json()
        first_name_ = requests_get_json['data']['first_name']
        print(first_name_)

        headers_request = {'my-token':'65c3245f-19e5b4bd1e9252f467b4eb93', 'user-agent':'python-requests/3.11'}
        r = requests.get('https://enhbs8zvxh569.x.pipedream.net/', headers=headers_request)
        print(r.json())
        print(r.headers)

        post_json_payload = {'name': 'srajan', 'job': 'lead'}
        response_post = requests.post('https://reqres.in/api/users', data=post_json_payload)
        print(response_post.text)

        user_id = 'flflfflflfll'
        url = f'https://reqrhhhhes.in/api/users/{user_id}'
        print(url)
        try:
                requests_get = requests.get(url)
                get_json = requests_get.json()
                print(get_json)
                requests_get.raise_for_status()
        except Exception as e:
                print('ERROR',type(e))

