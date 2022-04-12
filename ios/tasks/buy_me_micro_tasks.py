import webdriver as wdc
from tasks import general_micro_tasks as general

# First page :-
def pressAddItemBuyMe(driver):
    wdc.find_clickable_element(driver, "plusSign", True).click()

def getAllCartProductsNames(driver):
    return wdc.find_Elements(driver, "Item Name , description, and quantity, ex: 1 Kilo Hamor Fish")

def getAllCartProductsNotes(driver):
    return wdc.find_Elements(driver, "Note, ex: from SAMAKANA Restaurant")

def getAllCartProductsImageButtons(driver):
    return wdc.find_Elements(driver, "photo")

def getAllCartProductCancelButton(driver):
    return wdc.find_Elements(driver, "X")

def enterBuyMeProductName(productElement, productName):
    productElement.send_keys(productName)

def enterBuyMeProductNote(productNoteElement, productNote):
    productNoteElement.send_keys(productNote)

def pressBuyMeSelectProductImageButton(productImageButton):
    productImageButton.click()

def pressBuyMeCancelProductButton(productCancelButton):
    productCancelButton.click()
    general.getPictureFromDevice()

def checkIfNoItem(driver):
    return wdc.find_Elements(driver, "No Item On Cart")

# Second page :-

# Third page :-

