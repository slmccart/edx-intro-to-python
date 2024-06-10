from project import encode


def test_encode():
    assert encode("ABC", 2) == "CDE"
