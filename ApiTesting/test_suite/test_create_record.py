from dataclasses import asdict

import pytest
import requests

from ApiTesting.models.Requestmodel import RequestPayloadModel

@pytest.mark.regression
def test_post_call_validation(read_toml_file):
    base_url = read_toml_file['server']['url']
    print(base_url)
    post_api_endpoint = '/api/users'
    request_object = asdict(RequestPayloadModel("sj", "lead"))

    response = requests.post(base_url + post_api_endpoint, data=request_object)
    assert response.status_code == 201