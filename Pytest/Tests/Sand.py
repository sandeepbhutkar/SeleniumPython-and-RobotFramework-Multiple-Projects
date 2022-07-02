#this file will call fixture from "conftest.py" file
import pytest

def test_1(conf):
    print("test1")


def test_2(conf):
    print("test2")