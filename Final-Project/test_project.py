from project import encode
import pytest


def test_encode_word():
    assert encode("ABC", 2) == "CDE"


def test_encode_phrase():
    assert encode("This is a test", 2) == "VJKU KU C VGUV"


def test_encode_nonalpha():
    with pytest.raises(ValueError):
        encode("This is CS50", 2)
