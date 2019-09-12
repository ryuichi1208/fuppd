from .. import app
import pytest

class TestCommon:

    def test_get_resource(self):
        assert app.get_resource()

    def test_count(self):
        gc = app.gen_counter()
        for _ in range(10):
            gc()
        assert gc() == 11

    def test_count_init(self):
        gc = app.gen_counter()
        assert gc() == 1
