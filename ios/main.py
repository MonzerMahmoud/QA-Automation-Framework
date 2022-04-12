# iOS Environment

import webdriver as wdc
from samples import samples
from tasks import home_micro_tasks as home
from tasks import side_menu_micro_tasks as side_menu
driver = wdc.create_new_session()

samples.launchingSample(driver)
samples.loginSample(driver)
samples.makeBuyMeOrderSample(driver)
home.openSideMenu(driver)
side_menu.openMyOrders(driver)
print(driver.page_source)
# notificationPremission()
# skipTutorial()
# login()
# openBuyMe()
# selectTripType(False)
# pressAddItemBuyMe()
# pressAddItemBuyMe()
# pressAddItemBuyMe()

# productsNames = getAllCartProductsNames()
# productsNames[0].send_keys("Product 1")
# dismissKeyboard()


# pressContinueButton()
# locationPermission()
# pressContinueButton()
# for i in range(4):
#     enterBuyMeProductName(productsNames[i], "Product " + str(i+1))
    
# productsNotes = getAllCartProductsNotes()
# for i in range(4):
#     enterBuyMeProductNote(productsNotes[i], "Note " + str(i+1))

# #pressBuyMeCancelProductButton(getAllCartProductCancelButton()[0])

# pressBuyMeSelectProductImageButton(getAllCartProductsImageButtons()[0])



# W3CTouchAction(driver).tap(269, 517).Perform()
#a = wdc.TouchAction 
#wdc.quitting_session(driver)

