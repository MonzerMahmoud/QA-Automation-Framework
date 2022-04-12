import webdriver as wdc
from tasks import general_micro_tasks as general

def login(driver, mobile = "0129079882", password = "12345678"):
    wdc.find_clickable_element(driver, "Enter Mobile Number").send_keys(mobile)
    wdc.find_clickable_element(driver, "Enter Password").send_keys(password)
    general.dismissKeyboard(driver)
    wdc.find_clickable_element(driver, "LOGIN", True).click()