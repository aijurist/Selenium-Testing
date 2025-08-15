import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Login and verify product list on SauceDemo")
@allure.description("Logs in with valid credentials and checks that products are visible on the inventory page.")
@pytest.mark.login
def test_login_and_check_products(driver):
    wait = WebDriverWait(driver, 10)

    with allure.step("Open SauceDemo login page"):
        driver.get("https://www.saucedemo.com/")

    with allure.step("Enter valid credentials and click login"):
        username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

    with allure.step("Wait for product page to load"):
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

    with allure.step("Count number of products on page"):
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        allure.attach(str(len(products)), "Number of products", allure.attachment_type.TEXT)

    with allure.step("Take screenshot of product page"):
        allure.attach(driver.get_screenshot_as_png(),
                      name="Product Page Screenshot",
                      attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify that products are visible and URL is correct"):
        assert len(products) > 0, "No products found after login!"
        assert "inventory" in driver.current_url, "Did not navigate to product page"
