from plates import is_valid

def test_starts_with_two_letters():
    assert is_valid("AA2222")
    assert is_valid("CS50")
    assert not is_valid("2222")

def test_correct_number_of_characters():
    assert is_valid("AAAAAA")
    assert not is_valid("OUTATIME")
    assert is_valid("AA")
    assert not is_valid("H")

def test_no_numbers_in_the_middle():
    assert not is_valid("CS05")
    assert not is_valid("CS50P")

def test_no_punctuation():
    assert not is_valid("PI3.14")
