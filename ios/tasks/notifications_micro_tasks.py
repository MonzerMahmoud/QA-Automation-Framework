import webdriver as wdc

def readAllNotifications(driver):
    wdc.find_clickable_element(driver, "Read All", True).click()