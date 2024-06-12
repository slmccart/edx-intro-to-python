from project import encode
from project import decode
from project import validate


def test_encode_word():
    assert encode("ABC", 2) == "CDE"


def test_encode_phrase():
    assert encode("This is a test", 2) == "VJKU KU C VGUV"


def test_validate_valid():
    assert validate("This is a test")


def test_validate_nonalpha():
    assert not validate("This is CS50")


def test_decode_word():
    assert decode("CDE", 2) == "ABC"


def test_decode_phrase():
    assert decode("IQQF VGUV", 2) == "GOOD TEST"
