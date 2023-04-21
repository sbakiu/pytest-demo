import os

import pytest


@pytest.fixture
def project_id():
    print("setting project_id.")
    os.environ["PROJECT_ID"] = "test-project"
    yield
    print("unsetting project_id.")
    del os.environ['PROJECT_ID']
