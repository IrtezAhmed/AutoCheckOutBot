from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

url = "https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815"

#activate chrome

driver = webdriver.Chrome(executable_path="C:/Users/Nay-Nay/Documents/Scripts/executable/chromedriver.exe")

driver.get("https://www.walmart.com/account/login")

a = input("Sign into Walmart and PayPal. When you're done, type something here and let the computer do the rest: \n\n")

#access URL 
driver.get(url)

while 1:
    if "prod-countDownMessage" in driver.page_source:
        try: driver.get(url)
        except: input("Do captcha asap!")
        print("WORKING. PLEASE WAIT UNTIL ORDER IS AVAILABLE.")
        continue
    else:
        print("ORDER AVAILABLE GO GO GO GO!")
        break
    
    


#add the product to cart
try: addToCart = driver.find_element_by_xpath("//button[@class='button spin-button prod-ProductCTA--primary button--primary']").click() 
except: input("Manual mode active.")

#go to the checkout
GoToCheckout = driver.get("https://www.walmart.com/checkout")

a = input("TYPE WHEN READY")
'''
#autochoose delivery and hit continue

Continue = driver.find_element_by_xpath("//button[@class='button cxo-continue-btn button--primary']").click()
#select delivery address and hit continue
selectAddress = driver.find_element_by_class_name("checkbox-container")
ContinueAgain = driver.find_element_by_xpath("//button[@class='button button--primary']").click()'''

#enter payment method
morePayment = driver.find_element_by_xpath("//button[@class='payment-type-selector-option']").click()

#choose paypal
paypalchosen = driver.find_elements_by_class_name("paypal-button-text")

#continue payment
paypalchosen = driver.find_elements_by_class_name("[//button[@class='ppvx_btn']")

PayPalCheckout = driver.find_element_by_xpath("//button[@class='button ios-primary-btn-touch-fix hide-content-max-m checkoutBtn button--primary']").click()

a = input("Hey Crawly. Go Sign into BestBuy and PayPal. When you're done, type something here and let the computer do the rest: \n\n")

Agree = driver.find_element_by_xpath("//input[@class='btn full confirmButton continueButton']").click()

PlaceOrder = driver.find_element_by_xpath("//button[@class='button_2Xgu4 primary_oeAKs order-now regular_cDhX6']").click()

a = input("All done, type anything to exit.")

