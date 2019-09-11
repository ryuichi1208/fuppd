from .. import app
import pytest

def test_get_resource():
    assert app.get_resource()
