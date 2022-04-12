from tasks import general_micro_tasks as general
from tasks import launching_micro_tasks as launching
from tasks import registration_micro_tasks as registration
from tasks import buy_me_micro_tasks as buy_me
from tasks import home_micro_tasks as home

def launchingSample(driver):
    launching.notificationPremission(driver)
    launching.skipTutorial(driver)

def loginSample(driver):
    registration.login(driver)

def makeBuyMeOrderSample(driver):
    home.openBuyMe(driver)
    productsNames = buy_me.getAllCartProductsNames(driver)
    productsNames[0].send_keys("Girlfriend")
    general.dismissKeyboard(driver)
    general.pressContinueButton(driver)
    general.locationPermission(driver)
    general.getCurrentLocation(driver)
    general.pressContinueButton(driver)
    general.selectSelfContact(driver)
    general.pressContinueButton(driver)
    general.clickRequestSent(driver)

