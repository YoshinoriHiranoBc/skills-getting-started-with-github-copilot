from fastapi.testclient import TestClient
import pytest

from src import app as app_module
from src.app import app, activities
import copy


@pytest.fixture(autouse=True)
def client():
    """Provide a TestClient and ensure in-memory state is reset before each test."""
    # snapshot activities and restore after test to keep isolation
    original = copy.deepcopy(activities)
    yield TestClient(app)
    activities.clear()
    activities.update(original)
