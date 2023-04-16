from numb3rs import validate


def test_validate_correct():
    assert validate("255.255.255.0") == True

def test_validate_notNum():
    assert validate("cat") == False

def test_validate_numOutRange():
    assert validate("1000.00.0.1") == False

def test_validate_tooShort():
    assert validate("100.100") == False

def test_validate_firstTrue():
    assert validate("100.257.0.0") == False