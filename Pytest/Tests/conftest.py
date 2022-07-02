#all fixtures can be difined in tis file , name should be always "conftest.py"

import pytest

@pytest.fixture
def conf():
    print("i am from setup conftest")
    yield
    print("i am from setup yield conftest")

# this fixture will be called in "Sand.py" file
