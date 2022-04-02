import webdriver as wdc
import general_micro_tasks as general

def login(driver):
    wdc.find_clickable_element(driver, "Enter Mobile Number").send_keys("0129079882")
    wdc.find_clickable_element(driver, "Enter Password").send_keys("12345678")
    general.dismissKeyboard()
    wdc.find_clickable_element(driver, "LOGIN", True).click()