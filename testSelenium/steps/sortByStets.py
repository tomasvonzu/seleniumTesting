from behave import given, when, then
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.webdriver_manager import get_driver
driver = get_driver()

@given("the user wants to search an item")
def go_to_URL(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://highlifeshop.com/speedbird-cafe")
    time.sleep(2)
    close_cookies_button = context.driver.find_element(By.ID, "close-modal")
    close_cookies_button.click()


@when("the user sort by ascendent price")
def sort_by_ascendent_price(context):
    sort_button = context.driver.find_element(By.ID, "sorter")
    sort_button.click()
    sort_by_price_button = context.driver.find_element(By.XPATH, "//div[4]/main/div[2]/div[1]/div[2]/div[2]//option[3]")
    sort_by_price_button.click()
    close_cookies_button = context.driver.find_element(By.ID, "close-modal")
    close_cookies_button.click()

    
@then("the item with the lower price should appear first")
def verify_first_item_id(context):
    first_item = context.driver.find_element(By.CLASS_NAME ,"item.product.product-item")
    assert first_item.get_attribute("data-product-id") == "1353"

@when("the user sort by descendent price")
def sort_by_descendent_price(context):
    sort_button = context.driver.find_element(By.ID, "sorter")
    sort_button.click()
    sort_by_price_button = context.driver.find_element(By.XPATH, "//div[4]/main/div[2]/div[1]/div[2]/div[2]//option[3]")
    sort_by_price_button.click()

    close_cookies_button = context.driver.find_element(By.ID, "close-modal")
    close_cookies_button.click()

    descendent_price_button = context.driver.find_element(By.CLASS_NAME ,"action.sorter-action.sort-asc")
    descendent_price_button.click()

    
@then("the item with the higher price should appear first")
def verify_first_item_id(context):
    first_item = context.driver.find_element(By.CLASS_NAME ,"item.product.product-item")
    assert first_item.get_attribute("data-product-id") == "882"
