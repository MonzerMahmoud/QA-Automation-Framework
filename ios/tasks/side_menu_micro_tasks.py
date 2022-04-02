import webdriver as wdc 

def openHome(driver):
    wdc.find_clickable_element(driver, "Home", True).click()
    
def openMyOrders(driver):
    wdc.find_clickable_element(driver, "My Orders", True).click()

def openReceivedOrders(driver):
    wdc.find_clickable_element(driver, "ReceivedOrders", True).click()

def openMyProfile(driver):
    wdc.find_clickable_element(driver, "My Profile", True).click()

def openMyWallet(driver):
    wdc.find_clickable_element(driver, "My Wallet", True).click()

def openHelpAndLengal(driver):
    wdc.find_clickable_element(driver, "Help & Legal", True).click()

def openNotifications(driver):
    wdc.find_clickable_element(driver, "Notifications", True).click()

def openSettings(driver):
    wdc.find_clickable_element(driver, "Settings", True).click()

