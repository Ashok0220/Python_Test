import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_fristprogram():
    msg = "Hello"
    assert msg == "Hell", "Test faild becase string do not match"


def test_secondprogram():
    a=2
    b=6

    assert a+4 == 6, "Addition does not match"

def test_secondcreaditcard():
    print("Axis bank")