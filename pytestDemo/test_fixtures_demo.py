import pytest



@pytest.mark.usefixtures("setup")
class Testexample:

    def test_fixture_demo(self):
        print("i will execute step in fixture demo")

    def test_fixture_demo1(self):
        print("i will execute step in fixture demo")

    def test_fixture_demo2(self):
        print("i will execute step in fixture demo")

    def test_fixture_demo3(self):
        print("i will execute step in fixture demo")