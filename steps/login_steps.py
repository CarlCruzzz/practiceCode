from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('user is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/v1")
    time.sleep(2)

@when("user enters valid username and password")
def step_impl(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)

@when("click on the login button")
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

@then("user should be navigated to the product page")
def step_impl(context):
    title = context.driver.find_element(By.CLASS_NAME, "product_label").text
    assert title == "Products", f"Expected 'Products' but got '{title}'"
