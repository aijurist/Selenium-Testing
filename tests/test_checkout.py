import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Complete checkout flow on SauceDemo")
@allure.description("Logs in, adds a product to the cart, proceeds to checkout, and verifies order completion.")
@pytest.mark.checkout
def test_checkout_flow(driver):
    wait = WebDriverWait(driver, 10)

    with allure.step("Open login page"):
        driver.get("https://www.saucedemo.com/")

    with allure.step("Enter username and password"):
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")

    with allure.step("Click login button"):
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.url_contains("inventory"))

    with allure.step("Add first product to cart"):
        driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")[0].click()

    with allure.step("Go to cart page"):
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.url_contains("cart"))

    with allure.step("Click checkout"):
        driver.find_element(By.ID, "checkout").click()
        wait.until(EC.url_contains("checkout-step-one"))

    with allure.step("Fill in checkout information"):
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")

    with allure.step("Continue to overview page"):
        driver.find_element(By.ID, "continue").click()
        wait.until(EC.url_contains("checkout-step-two"))

    with allure.step("Finish the checkout"):
        driver.find_element(By.ID, "finish").click()
        wait.until(EC.url_contains("checkout-complete"))

    with allure.step("Verify completion message"):
        complete_msg = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert "THANK YOU" in complete_msg.upper()

    with allure.step("Attach final checkout screenshot"):
        allure.attach(driver.get_screenshot_as_png(),
                      name="Order Confirmation",
                      attachment_type=allure.attachment_type.PNG)
