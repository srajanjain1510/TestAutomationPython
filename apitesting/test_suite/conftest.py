import pytest
import toml


@pytest.fixture
def read_toml_file():
    f = open('../config/config.toml')
    config = toml.load(f)
    yield config
    f.close()
