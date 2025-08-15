from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkout_flow(driver):
    wait = WebDriverWait(driver, 10)

    # Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory"))

    # Add product to cart
    driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")[0].click()

    # Go to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("cart"))

    # Checkout
    driver.find_element(By.ID, "checkout").click()
    wait.until(EC.url_contains("checkout-step-one"))

    # Fill checkout info
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Finish checkout
    wait.until(EC.url_contains("checkout-step-two"))
    driver.find_element(By.ID, "finish").click()
    wait.until(EC.url_contains("checkout-complete"))

    # Verify completion message
    complete_msg = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "THANK YOU" in complete_msg.upper()
