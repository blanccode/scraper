from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions, Chrome, Firefox
from requests import request as r
from bs4 import BeautifulSoup as bs
import ctypes
from functions import *
# from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

# req_proxy = (
#     RequestProxy()
# )  # you may get different number of proxy when  you run this at each time
# proxies = req_proxy.get_proxy_list()  # this will create proxy list

# PROXY = proxies[0].get_address()

# ips = []
# for proxy in proxies:
#     # if proxy.country == 'Germany':
#     ips.append(proxy.get_address())

# url = "http:/httpbin.org/ip"

# for ip in range(len(ips)):
#     print("Request Number : " + str(ip+1))
#     proxy = ips[ip]

#     try:
#         response = requests.get(url, proxies = {"http":proxy, "https": proxy})
#         print(response.json())
#     except:
#         print("not available")

# def refreshCheckItemAvailability(driver,url):

#     # driver = driver
  
#     # # COOKIE ACCEPT
#     # cookieForm = driver.find_element_by_xpath(
#     #     '//*[@id="privacy-layer__wrapper"]/form'
#     # )
#     # acceptBtn = driver.find_element_by_css_selector(
#     #     "#privacy-layer-accept-all-button"
#     # )

#     # ActionChains(driver).move_to_element(cookieForm).click(acceptBtn).perform()

#     toCartBtn = False
#     while not toCartBtn:
#         try:
#             refreshLimit = 4
#             for x in range(0,4):
#                 # /////// WAIT TILL PRODUCT IS AVAILABLE & DETECT ADD TO CART BTN  ////////
#                 # p = driver.findElement(By.cssSelector("p")).getText()
#                 # data = driver.find_element_by_tag_name('p')
                
#                 # moveToBtn = WebDriverWait(driver,1).until(
#                 #         EC.presence_of_element_located(
#                 #             (By.ID, 'pdp-add-to-cart-button')
#                 #         )
#                 #     )
#                 merkzettelBtn = driver.find_element_by_css_selector(
#                     ".detail-error--headline"
#                 )
                
#                 print("article is not in stock stock.")
#                 time.sleep(2)
#                 driver.refresh()
#                 # moveToBtn = driver.find_element_by_css_selector(
#                 #     "#pdp-add-to-cart-button"
#                 # )
#             driver.quit()
#             rotateIp(url)  
            

#                 # time.sleep(3)

#                 # driver.refresh()

#                 # wait for data to be loaded
#                 # WebDriverWait(driver, delay).until(
#                 #     EC.presence_of_element_located((By.CSS_SELECTOR, selector))
#                 # )
#         except:
#             addToCartBtn = driver.find_element_by_css_selector(
#                 "#pdp-add-to-cart-button"
#             )
#             addToCartBtn.click()
#             print("Articel found and Btn clicked")

#             showPopup()

#             toCartBtn = True
#             # else:
#             #     print('esle')
#             #     html = driver.page_source
#             # # finally:
#             # #     driver.quit()
#             # #
#             # if html:
#             #     soup = BeautifulSoup(html, 'lxml')
#             #     raw_data = soup.select_one(selector).text
#             #     data = json.loads(raw_data)
#             # #
#             #     import pprint
#             #     print(data)


class Scraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(
            executable_path="/Users/hamza/downloads/geckodriver"
        )


# class Mediamarkt(Scraper):
#     def fillForm(self):
#         pass
#         driver = self.driver

#         zurKasseBtn = WebDriverWait(driver, 3).until(
#             EC.presence_of_element_located(
#                 (
#                     By.XPATH,
#                     '//*[@id="root"]/div[2]/div[4]/div[1]/div/div/div/div/div[8]/div/div/div/div/div[4]/div/button',
#                 )
#             )
#         )

#         ActionChains(driver).move_to_element(zurKasseBtn).click(zurKasseBtn).perform()
#         print("btn clicked")

#         time.sleep(1)
#         AnmeldungBtn = WebDriverWait(driver, 3).until(
#             EC.presence_of_element_located((By.ID, "mms-login-form__login-button"))
#         )

#         ActionChains(driver).move_to_element(AnmeldungBtn).click(AnmeldungBtn).perform()
#         print("slept for seconds")

#         username = driver.find_element_by_id("mms-login-form__email")
#         password = driver.find_element_by_id("mms-login-form__password")
#         # fill form and click login btn
#         username.send_keys("fatih.cetinkaya.1999@gmail.com")
#         password.send_keys("Oecfzqv713844")
#         driver.find_element_by_id("mms-login-form__login-button").click()

#         def kreditkarte():
#             pass
#             kreditkarte = driver.find_element_by_xpath(
#                 "//*[contains(text(), 'Kreditkarte')]"
#             )
#             return kreditkarte

#         visaBtn = WebDriverWait(driver, 3).until(
#             EC.presence_of_element_located((By.XPATH, "//div[text() = 'Kreditkarte']"))
#         )
#         print("visa found")
#         ActionChains(driver).move_to_element(visaBtn).click(visaBtn).perform()
#         weiterBtn = driver.find_element_by_xpath(
#             '//*[@id="root"]/div[2]/div[3]/div[1]/div/div[2]/div/div[11]/div/button'
#         )

#         ActionChains(driver).move_to_element(visaBtn).click(visaBtn).perform()
#         ActionChains(driver).click(weiterBtn).perform()

#         driver.find_element_by_xpath(
#             '//*[@id="root"]/div[2]/div[3]/div[1]/div/div[2]/div/div[8]/div/div/div/div/div[4]/div/button'
#         ).click()
#         print("payment chosen and item added to basket")

#     def scrapeMediamarkt(self):
#         pass
        
#         url = self.url
        
#         driver.get(url)
        
#         refreshCheckItemAvailability(driver)

#     # makeRequest()
#     # scrapeMediamarkt()

class Asus(Scraper):
    def scrapeAsus(self):
        url = self.url
        driver = self.driver
        driver.get(url)
        refreshCheckItemAvailability(driver,url)

        
class Alternate(Scraper):
    def scrapeAlternate(self):
        url = self.url
        driver = self.driver
        driver.get(url)
        refreshCheckItemAvailabilityAlternate(driver,url)

        
class Amazon(Scraper):
    def scrapeAmazon(self):
        url = self.url
        driver = self.driver
        driver.get(url)
        refreshCheckItemAvailabilityAmazon(driver,url)

        