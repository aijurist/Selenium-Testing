import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Login Test for SauceDemo")
@allure.description("Verifies login functionality with valid credentials.")
def test_login(driver):
    wait = WebDriverWait(driver, 10)

    with allure.step("Open login page"):
        driver.get("https://www.saucedemo.com/")

    with allure.step("Enter username and password"):
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")

    with allure.step("Click login button"):
        driver.find_element(By.ID, "login-button").click()

    with allure.step("Verify inventory page loaded"):
        wait.until(EC.url_contains("inventory"))
        assert "inventory" in driver.current_url

    with allure.step("Take screenshot"):
        allure.attach(driver.get_screenshot_as_png(), name="Login Page", attachment_type=allure.attachment_type.PNG)
