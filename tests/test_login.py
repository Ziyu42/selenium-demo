from pages.login_page import LoginPage

def test_login_success(driver):
    login_page = LoginPage(driver)
    driver.get("https://the-internet.herokuapp.com/login")
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_flash_message()

def test_login_fail(driver):
    login_page = LoginPage(driver)
    driver.get("https://the-internet.herokuapp.com/login")
    login_page.login("wrong", "wrong")
    assert "Your username is invalid!" in login_page.get_flash_message()
