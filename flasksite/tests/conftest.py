import pytest

from flasksite import app


@pytest.fixture
def app():
    return app


