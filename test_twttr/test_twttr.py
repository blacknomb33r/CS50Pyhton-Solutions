from twttr import shorten
import pytest

def test_lowerCase():
    assert shorten("twitter") == "twttr"

def test_upperCase():
    assert shorten("Twitter") == "Twttr"

def test_None():
    assert shorten("") == ""

def test_allUpperCase():
    assert shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("123") == "123"

def test_symbols():
    assert shorten("...") == "..."

def test_vowelUpper():
    assert shorten("TwittEr") == "Twttr"