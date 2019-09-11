from .. import app
import pytest

class TestCommon:

    def test_get_resource(self):
        assert app.get_resource()
