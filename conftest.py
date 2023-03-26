import pytest
from selenium import webdriver


# инициализируем сессию
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()  # закрываем сессию
