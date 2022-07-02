import pytest

@pytest.yield_fixture()
def setup():
    print("setup")
    yield
    print("yield")

def test_1(setup):
    print("test1")

def test_2(setup):
    print("test2")


