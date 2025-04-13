import pytest


#Data driver fixture

@pytest.mark.usefixtures("data_load")
class Testexample:
    def test_data(self, data_load):
        print(data_load[2])



def test_dare(crossbrowser):
    print(crossbrowser)
