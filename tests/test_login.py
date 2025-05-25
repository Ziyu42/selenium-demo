from pages.login_page import LoginPage

def test_login_success(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_flash_message()
    assert "/secure" in login_page.get_current_url()

def test_login_failure(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "wrongpass")
    assert "Your password is invalid!" in login_page.get_flash_message()


def test_logout_success(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "SuperSecretPassword!")

    #登出
    login_page.logout()
    flash_message_after_logout = login_page.get_flash_message()
    assert "You logged out of the secure area!" in flash_message_after_logout

def test_after_login_logout_button(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert login_page.is_logout_button_displayed() is True


def test_after_login_secure_area_exist(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert login_page.secure_area().is_displayed()

def test_login_failure_message(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "wrongpass")

    assert "flash error" in login_page.get_flash_attribute()
    
def test_login_password_blank(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "")

    assert "Your password is invalid!" in login_page.get_flash_message()


def test_login_failure_three_times_reflash_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(driver)
    login_page.perform_failed_login_attempts("tomsmith", "wrongpass",3)
    login_page.refresh_page()
    current_url = login_page.is_on_login_page()
    assert current_url

    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_flash_message()


def test_login_failure_mesage_red(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "wrongpass")

    print(f"錯誤訊息顏色: {login_page.get_flash_background()}")

    assert "rgba(198, 15, 19" in login_page.get_flash_background() or "rgb(198, 15, 19" in login_page.get_flash_background()
