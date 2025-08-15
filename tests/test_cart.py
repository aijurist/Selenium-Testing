import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Add product to cart on SauceDemo")
@allure.description("Logs in, adds a product to cart, and verifies it appears in the cart.")
@pytest.mark.cart
def test_add_to_cart(driver):
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
        add_button = driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")[0]
        product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text
        allure.attach(product_name, "Selected Product", allure.attachment_type.TEXT)
        add_button.click()

    with allure.step("Go to cart page"):
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.url_contains("cart"))

    with allure.step("Verify product is in cart"):
        cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        assert any(product_name == item.text for item in cart_items), "Product not found in cart"

    with allure.step("Take final screenshot"):
        allure.attach(driver.get_screenshot_as_png(),
                      name="Cart Screenshot",
                      attachment_type=allure.attachment_type.PNG)
