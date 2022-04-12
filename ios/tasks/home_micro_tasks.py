import webdriver as wdc

def openSideMenu(driver):
    if wdc.find_clickable_element(driver, "Side Menu", True) is not None:
        wdc.find_clickable_element(driver, "Side Menu", True).click()

def openNotificationsFromHome(driver):
    wdc.find_clickable_element(driver, "notificationWithOutCircle", True).click()

def openSendRecieve(driver):
    wdc.find_clickable_element(driver, "Send/Receive", True).click()

def openBuyMe(driver):
    wdc.find_clickable_element(driver, "Buy Me", True).click()