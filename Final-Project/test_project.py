from project import encode
from project import decode
import pytest


def test_encode_word():
    assert encode("ABC", 2) == "CDE"


def test_encode_phrase():
    assert encode("This is a test", 2) == "VJKU KU C VGUV"


def test_encode_nonalpha():
    with pytest.raises(ValueError):
        encode("This is CS50", 2)


def test_decode_word():
    assert decode("CDE", 2) == "ABC"


def test_decode_phrase():
    assert decode("IQQF VGUV", 2) == "GOOD TEST"
