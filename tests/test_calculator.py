from string_calculator.calculator import add
import pytest


def test_add():
    assert add("1") == 1
    assert add("//;\n1000,1;2")==3
    assert add("//[:D][%]\n1:D2%3")==6