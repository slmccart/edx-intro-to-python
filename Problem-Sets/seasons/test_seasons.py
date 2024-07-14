from seasons import convert_input
from seasons import time_delta_in_minutes
from seasons import convert_minutes_to_words
from datetime import date
import pytest

def test_convert_valid_input():
    assert convert_input("1999-01-01") == date(1999, 1, 1)

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert_input("January 1, 1999")
    with pytest.raises(ValueError):
        convert_input("1999-1-1")

def test_time_delta_in_minutes():
    assert time_delta_in_minutes(date(1999, 1, 1), date(2000, 1, 1)) == 525600

def test_convert_minutes_to_words():
    assert convert_minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
