import pytest

def test_1():
    assert 11==11

def test_2():
    assert "Sandeep"=="sandeep"
@pytest.mark.smoke
def test_3():
    assert "krish"=="krish"



#pytest -v -s --html=.\Pytest\Reports\mark.html .\Pytest\Tests\Test_Mark.py -m smoke
