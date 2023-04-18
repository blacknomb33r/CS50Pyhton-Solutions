from um import count


def testOnly2():
    assert count("um") == 1
def testUmSent():    
    assert count(" um ") == 1
def testUmSpeChar():    
    assert count("Um") == 1
def testUm():
    assert count("yummy") == 0