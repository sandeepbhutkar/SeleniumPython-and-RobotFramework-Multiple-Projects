import pytest
from selenium import webdriver
#pip install pytest-xdist
#pytest -v -s --html=.\Pytest\Reports\Parallel1.html .\Pytest\Tests\Test_ParallelRun.py -n 3
#will open 3 browser parallel

def test_Google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    driver.close()

def test_Bing():
    driver = webdriver.Chrome()
    driver.get("https://www.bing.com")
    assert driver.title == "Bing"
    driver.close()

def test_Rediff():
    driver = webdriver.Chrome()
    driver.get("https://www.rediff.com/")
    assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.close()



