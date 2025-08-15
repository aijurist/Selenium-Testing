from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    # Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory"))

    # Add first product
    add_button = driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")[0]
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text
    add_button.click()

    # Go to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("cart"))

    # Verify product in cart
    cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert any(product_name == item.text for item in cart_items)
