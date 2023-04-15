from plates import is_valid

def testTooLong():
    assert is_valid("ASBS111") == False

def testTooShort():
    assert is_valid("A") == False

def testValidInput():
    assert is_valid("CS50") == True

def testInvalidInput():
    assert is_valid("121212") == False

def testWrongNumberPlace():
    assert is_valid("CS05") == False

def testAlphaNum():
    assert is_valid("CS$50") == False

def testAlpha():
    assert is_valid("12ASSA") == False

def testNum():
    assert is_valid("AAA22A") == False
