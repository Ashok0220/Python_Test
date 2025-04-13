from webbrowser import Chrome

import pytest
from selenium import webdriver
from selenium.webdriver import chrome

# if any path issue un command below line
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")

def pytest_addoption(parser):
    parser.addoption(
    "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browser_instance(request):
    # browser_name = request.config.getoption("browser_name")
    # if browser_name == "chrome":
    #     driver = webdriver.Chrome()
    #     driver.implicitly_wait(5)
    # else:
    #     driver = webdriver.Firefox()
    #     driver.implicitly_wait(5)
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")  # Use "--" for headless argument
        # driver = webdriver.Chrome(options=chrome_options)  # Pass options here
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()