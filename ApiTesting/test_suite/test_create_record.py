import pytest
import requests

from ApiTesting.models.Requestmodel import RequestPayloadModel

@pytest.mark.regression
def test_post_call_validation(read_toml_file):
    base_url = read_toml_file['server']['url']
    print(base_url)
    post_api_endpoint = '/api/users'
    request_object = RequestPayloadModel("sj", "lead")
    payload = request_object.to_json()
    response = requests.post(base_url + post_api_endpoint, payload)
