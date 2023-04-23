from seasons import numToWord


def testIt():
    assert numToWord(10243) == "Fourteen million, seven hundred forty-nine thousand, nine hundred twenty minutes"
    assert numToWord(365) == "Five hundred twenty-five thousand, six hundred minutes"