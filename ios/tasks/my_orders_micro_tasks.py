import webdriver as wdc

def openPastOrders(driver):
    wdc.find_clickable_element(driver, "Past", True).click()