import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Sort products by price: Low to High")
@allure.description("Logs in and verifies that products are correctly sorted from lowest to highest price.")
@pytest.mark.sorting
def test_sort_products_low_to_high(driver):
    wait = WebDriverWait(driver, 10)

    with allure.step("Login to SauceDemo"):
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.url_contains("inventory"))

    with allure.step("Select sorting option: Price (low to high)"):
        select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value("lohi")

    with allure.step("Extract prices from product list"):
        prices = [float(price.text.strip("$")) for price in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
        allure.attach(str(prices), "Extracted Prices", allure.attachment_type.TEXT)

    with allure.step("Take screenshot of sorted products"):
        allure.attach(driver.get_screenshot_as_png(),
                      name="Sorted Products Screenshot",
                      attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify prices are sorted in ascending order"):
        assert prices == sorted(prices), f"Prices not sorted correctly: {prices}"
