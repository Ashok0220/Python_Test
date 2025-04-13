#Any pytest file should be start with _test or end with test_
#  Pytest method name should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s logs out put
# -v stands for more info metadata
# we can run specific file with py.test filename
# we can mention mark (tags) @pytest.mark smoke and then run with -m
# we can skip method using @pytest.mark.skip
# py.test.mark.xfail
# fixture are used as setup and tear down methods for test cases - conftest file to generalize file
# fixture and  make it available to all test cases

# Data driven and parameterization can be done with return statement in tuple formate.
# when you define fixture scope to class only, it will run once before class is initiate and at the end.



import pytest


@pytest.mark.smoke
def test_fristprogram(setup):
    print("Hello")



def test_fristprograms():
    print("Good Morning")



@pytest.mark.xfail
def test_fristcreaditcard():
    print("HDFC")