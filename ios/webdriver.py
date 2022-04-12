import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import constants

desired_caps = dict(
    platformName=constants.PLATFORM_NAME,
    platformVersion=constants.PLATFORM_VERSION,
    automationName=constants.AUTOMATION_NAME,
    deviceName=constants.DEVICE_NAME,
    app=constants.APP
)

def create_new_session():
    driver = webdriver.Remote(constants.SERVER_URL, desired_caps)
    return driver

def quitting_session(driver):
    driver.quit()

def find_clickable_element(driver, id, withWait = False):
    if withWait:
        try:
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, id)))
        except:
            print("could not find element " + id)
            print("Page Source ::: \n" + driver.page_source)
            
        
    else:
        return driver.find_element(AppiumBy.ACCESSIBILITY_ID, id)

def find_Elements(driver, id):
    return driver.find_elements(AppiumBy.ACCESSIBILITY_ID, id)

def check_Element(driver, id):
    if driver.find_element(AppiumBy.ACCESSIBILITY_ID, id):
        return True
    else:
        return False
