import pytest


#class testFixture():
@pytest.fixture()
def setup():
    print("setup")    # will run before every method/function

def test1(setup):
    print("test1")


def test2(setup):
    print("test2")




