import unittest


class TestNormal(unittest.TestCase):
    def test_fail(self):
        assert 1 == 2

    def test_succ(self):
        assert 2 == 2
