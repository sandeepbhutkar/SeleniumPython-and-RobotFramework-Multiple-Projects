from selenium import webdriver
import pytest
import pytest_html
import random, time, queue
import multiprocessing
multiprocessing.set_start_method('spawn')

from multiprocessing.managers import BaseManager


def test_google1():
    print("google1")
def test_google2():
    print("google2")


# to run
#pytest -v -s --html=report.html Pytest_test.py
#in specific folder
#pytest -v -s --html=.\Pytest\Reports\GoogleReport1.html .\Pytest\Tests\Pytest_test.py
#Naveens Pytest
#Running options
#py.test --- will run all test cases in folder
#py.test --html=.\Pytest\Reports\GoogleReport1.html   ---- generate reports
#py.test  --html=.\Pytest\Reports\GoogleReport1.html -k yield      ----- runs test case file matching "yield" k=keyword
#pytest -v -s --html=.\Pytest\Reports\mark.html .\Pytest\Tests\Test_Mark.py -m smoke
