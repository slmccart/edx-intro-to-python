from numb3rs import validate

def test_valid():
    assert validate("1.2.3.4")
    assert validate("255.255.255.255")
    assert validate("0.0.0.0")

def test_only_contains_digits():
    assert not validate("a.b.c.d")
    assert not validate("cat")

def test_octet_contains_at_most_3_digits():
    assert not validate("1111.0.0.0")
    assert not validate("0.1111.0.0")
    assert not validate("0.0.1111.0")
    assert not validate("0.0.0.1111")

def test_limit_of_255():
    assert not validate("256.0.0.0")
    assert not validate("0.256.0.0")
    assert not validate("0.0.256.0")
    assert not validate("0.0.0.256")
