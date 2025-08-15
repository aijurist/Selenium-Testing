from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_sort_products_low_to_high(driver):
    wait = WebDriverWait(driver, 10)

    # Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory"))

    # Sort by price (low to high)
    select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    select.select_by_value("lohi")

    # Get prices and verify sorted order
    prices = [float(price.text.strip("$")) for price in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
    assert prices == sorted(prices), f"Prices not sorted correctly: {prices}"
