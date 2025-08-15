import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("username,password,expected_url", [
    ("standard_user", "secret_sauce", "inventory"),  # valid
    ("locked_out_user", "secret_sauce", "error"),    # locked user
    ("invalid_user", "wrong_pass", "error"),         # invalid creds
])
def test_login(driver, username, password, expected_url):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    if expected_url == "inventory":
        wait.until(EC.url_contains("inventory"))
        assert "inventory" in driver.current_url
    else:
        error_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
        assert error_elem.is_displayed()
