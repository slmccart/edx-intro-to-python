from cipher import Cipher


def test_encode_char_low_wrap():
    cipher = Cipher(-1)
    assert cipher.encode("A") == "Z"
    cipher = Cipher(-2)
    assert cipher.encode("A") == "Y"


def test_encode_char_high_wrap():
    cipher = Cipher(2)
    assert cipher.encode("Z") == "B"
    cipher = Cipher(1)
    assert cipher.encode("Z") == "A"


def test_encode_char_no_wrap():
    cipher = Cipher(2)
    assert cipher.encode("A") == "C"


def test_encode_word():
    cipher = Cipher(4)
    assert cipher.encode("HELLO") == "LIPPS"


def test_decode_word():
    cipher = Cipher(4)
    assert cipher.decode("LIPPS") == "HELLO"


def test_decode_char_high_wrap():
    cipher = Cipher(1)
    assert cipher.decode("A") == "Z"
    cipher = Cipher(2)
    assert cipher.decode("A") == "Y"


def test_decode_char_low_wrap():
    cipher = Cipher(-2)
    assert cipher.decode("Z") == "B"
    cipher = Cipher(-1)
    assert cipher.decode("Z") == "A"
