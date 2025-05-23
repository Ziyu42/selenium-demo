import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5) # 設定隱式等待為 5 秒
    yield driver
    driver.quit()
