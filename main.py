from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://www.saucedemo.com/")

#Authorization
username = driver.find_element(By.CSS_SELECTOR, '[data-test = username]')
password = driver.find_element(By.CSS_SELECTOR, '[data-test = password]')
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

#Select the product and add to cart
cart_item = driver.find_element(By.CSS_SELECTOR, '[data-test = inventory-item-name')
assert cart_item.text == "Sauce Labs Backpack"
cart_item.click()

#Add to cart
add_button = driver.find_element(By.CSS_SELECTOR, '[data-test = add-to-cart]')
add_button.click()

#Go to cart
cart_button = driver.find_element(By.CSS_SELECTOR, "[data-test = shopping-cart-link]")
cart_button.click()

#Check product in cart
cart_item = driver.find_element(By.CSS_SELECTOR, '[data-test = inventory-item-name]')
assert cart_item.text == 'Sauce Labs Backpack'

#Checkout button
checkout_button = driver.find_element(By.CSS_SELECTOR, '[data-test = checkout]')
checkout_button.click()
time.sleep(2)

first_name = driver.find_element(By.CSS_SELECTOR, "[data-test = firstName]")
last_name = driver.find_element(By.CSS_SELECTOR, "[data-test = lastName]")
postal_code = driver.find_element(By.CSS_SELECTOR, "[data-test = postalCode")

#Checkout
first_name.send_keys("Test")
last_name.send_keys("User")
postal_code.send_keys("12345")


continue_button = driver.find_element(By.CSS_SELECTOR, "[data-test = continue]")
continue_button.click()

finish_button = driver.find_element(By.CSS_SELECTOR, "[data-test = finish]")
finish_button.click()

complete_text = driver.find_element(By.CSS_SELECTOR, "[data-test = complete-header]")
assert complete_text.text == "Thank you for your order!"

driver.quit()