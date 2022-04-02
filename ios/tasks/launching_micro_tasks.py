import webdriver as wdc

def notificationPremission(driver):
    wdc.find_clickable_element(driver, "Allow", True).click()

def skipTutorial(driver):
    wdc.find_clickable_element(driver, "Skip Now", True).click()
