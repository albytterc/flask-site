import pytest

from src import app


@pytest.fixture
def app():
    return app


