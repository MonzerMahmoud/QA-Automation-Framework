import webdriver as wdc

def openPastOrders(driver):
    wdc.find_clickable_element(driver, "Past", True).click()

def openActiveOrders(driver):
    wdc.find_clickable_element(driver, "Active", True).click()

def openEditOrder(driver):
    wdc.find_clickable_element(driver, "Edit", True).click()

def openDetailsOfOrder(driver):
    wdc.find_clickable_element(driver, "View Details", True).click()

def cancelOrder(driver):
    wdc.find_clickable_element(driver, "Cancel", True).click()