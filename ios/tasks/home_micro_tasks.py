import webdriver as wdc

def openNotificationsFromHome(driver):
    wdc.find_clickable_element(driver, "notificationWithOutCircle", True).click()

def openSendRecieve(driver):
    wdc.find_clickable_element(driver, "Send/Receive", True).click()

def openBuyMe(driver):
    wdc.find_clickable_element(driver, "Buy Me", True).click()