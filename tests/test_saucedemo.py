from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_and_check_products(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Open SauceDemo
    driver.get("https://www.saucedemo.com/")

    # 2. Login
    username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    # 3. Wait for product page
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

    # 4. Count products
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    driver.save_screenshot("saucedemo_products.png")

    # 5. Assertions
    assert len(products) > 0, "No products found after login!"
    assert "inventory" in driver.current_url, "Did not navigate to product page"
