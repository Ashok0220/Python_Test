import pytest


# @pytest.fixture(scope="class") it's used class leave execute

@pytest.fixture()
def setup():
    print("i will executing first")
    yield
    print("i will execute last")


#Data driver fixture
@pytest.fixture()
def data_load():
    print("user profile data bring here")
    return ["Ashok", "Babu", "Ashokautomation.com"]



@pytest.fixture(params=[("chrome", "Ashok", "Babu"), ("firefox","Ashokautomation.com"), ( "IE", "java")])
def crossbrowser(request):
    return request.param
