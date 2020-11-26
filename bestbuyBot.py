from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

path = str(input("Please input the path of your chromedriver.exe file."))
url = str(input("Enter the full URL (including https) of the product you want to purchase (BestBuy Canada Only): \n\n "))

#activate chrome

driver = webdriver.Chrome('C:/Users/Nay-Nay/Documents/Scripts/executable/chromedriver.exe')

driver.get("https://www.bestbuy.ca/account/en-ca")

a = input("Hey there solider. Sign into BestBuy and PayPal. When you're done, type something here and let the computer do the rest: \n\n")

#access URL 
driver.get(url)

while 1:
    if "button_2Xgu4 primary_oeAKs addToCartButton_1DQ8z addToCartButton regular_cDhX6 disabled_XY3i_" in driver.page_source:
        driver.get(url)
        print("WORKING. PLEASE WAIT UNTIL ORDER IS AVAILABLE.")
        continue
    else:
        print("ORDER AVAILABLE GO GO GO GO!")
        break

addToCart = driver.find_element_by_xpath("//button[@class='button_2Xgu4 primary_oeAKs addToCartButton_1DQ8z addToCartButton regular_cDhX6']").click()

time.sleep(3)

Basket = driver.get("https://www.bestbuy.ca/en-ca/basket")

PayPalCheckout = driver.find_element_by_xpath("//a[@class='paypalButton_3YgO1']").click()

time.sleep(8)

Agree = driver.find_element_by_xpath("//input[@class='btn full confirmButton continueButton']").click()

PlaceOrder = driver.find_element_by_xpath("//button[@class='button_2Xgu4 primary_oeAKs order-now regular_cDhX6']").click()

a = input("All done, type anything to exit.")

driver.close()

