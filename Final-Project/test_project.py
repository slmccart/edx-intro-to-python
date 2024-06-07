from project import encode


def test_encode_char_low_wrap():
    assert encode("A", -1) == "Z"
    assert encode("A", -2) == "Y"


def test_encode_char_high_wrap():
    assert encode("Z", 2) == "B"
    assert encode("Z", 1) == "A"


def test_encode_char_no_wrap():
    assert encode("A", 2) == "C"


def test_encode_word():
    assert encode("HELLO", 4) == "LIPPS"
