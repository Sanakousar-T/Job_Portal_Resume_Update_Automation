from selenium.webdriver import ChromeOptions,Chrome
import pytest

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture
def launch(request):
    driver = Chrome(opts)
    driver.get(request.param)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()