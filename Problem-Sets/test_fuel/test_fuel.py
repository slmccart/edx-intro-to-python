from fuel import convert
from fuel import gauge
import pytest

def test_valid_numbers():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("0/100") == 0
    assert convert("100/100") == 100

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_fraction_above_100():
    with pytest.raises(ValueError):
        convert("2/1")

def test_nonnumeric_inputs():
    with pytest.raises(ValueError):
        convert("b/1")
    with pytest.raises(ValueError):
        convert("1/b")

def test_gauge_nominal():
    assert gauge(50) == "50%"
    assert gauge(2) == "2%"

def test_gauge_boundaries():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
