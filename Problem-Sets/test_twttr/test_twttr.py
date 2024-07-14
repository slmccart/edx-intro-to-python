from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("") == ""
    assert shorten("CS50") == "CS50"
    assert shorten("hello, world") == "hll, wrld"
