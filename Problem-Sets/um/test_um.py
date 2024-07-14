from um import count

def test_um_surrounded_by_spaces():
    assert count(" um ") == 1

def test_um_in_another_word():
    assert count(" album ") == 0
    assert count("album") == 0
    assert count("yummy") == 0

def test_um_followed_by_punctuation():
    assert count("um?") == 1
    assert count("Um.") == 1

def test_full_sentences():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
