import webdriver as wdc

def dismissKeyboard(driver):
    wdc.find_clickable_element(driver, "Done", True).click()

def locationPermission(driver):
    wdc.find_clickable_element(driver, "Allow Once", True).click()

def selectTripType(driver, isOneWay = True):
    if isOneWay:
        wdc.find_clickable_element(driver, "One Way Trip", True).click()
    else:
        wdc.find_clickable_element(driver, "Round Trip", True).click()

def getCurrentLocation(driver):
    wdc.find_clickable_element(driver, "gpsCircle", True).click()

def pressHomeButton(driver):
    wdc.find_clickable_element(driver, "home", True).click()

def confirmPickupLocation(driver):
    wdc.find_clickable_element(driver, "Confirm Pickup Location", True).click()

def getPictureFromDevice(driver):
    wdc.find_clickable_element(driver, "Choose From Camera Roll", True).click()
    photosPremission()
    wdc.find_clickable_element(driver, "Photo", True).click()

def photosPremission(driver):
    wdc.find_clickable_element(driver, "Allow Access to All Photos", True).click() 

def pressContinueButton(driver):
    wdc.find_clickable_element(driver, "Continue", True).click()

def selectSelfContact(driver):
    wdc.find_clickable_element(driver, "You", True).click()

def clickRequestSent(driver):
    wdc.find_clickable_element(driver, "Request sent successfully", True).click()

