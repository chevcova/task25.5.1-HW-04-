import pytest as pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome(r'C:\Users\Клавдия\PycharmProjects\pythonProject24\chromedriver_win32\chromedriver.exe')
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')
    yield driver
    driver.quit()