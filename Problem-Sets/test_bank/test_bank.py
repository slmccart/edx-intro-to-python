from bank import value

def test_hello():
    assert value("Hello, David") == 0
    assert value("hello, David") == 0

def test_hey():
    assert value("Hey, David") == 20
    assert value("hey, David") == 20

def test_greetings():
    assert value("Greetings, David") == 100
    assert value("greetings, David") == 100
