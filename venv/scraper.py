import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import requests
import time
from selenium.webdriver import ChromeOptions, Chrome
import ctypes
import threading

from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list

PROXY = proxies[0].get_address()


ips = []
for proxy in proxies:
    # if proxy.country == 'Germany':
    ips.append(proxy.get_address())



for ip in ips:
    time.sleep(2)
    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":ip,
        "ftpProxy":ip,
        "sslProxy":ip,
        
        "proxyType":"MANUAL",
        
    }
    webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True

    driver = webdriver.Chrome(executable_path="/Users/hamza/downloads/chromedriver")
    driver.get('https://www.mediamarkt.de/')


    # merkBtn = WebDriverWait(driver, 99).until(
    #         EC.presence_of_element_located((By.ID, 'pdp-single-wishlist-button'))
    #     )
    time.sleep(4)
    driver.quit()
    
# # Simple usage with built-in WebDrivers:
# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(chrome_options=options, executable_path="/Users/hamza/downloads/chromedriver")
# driver.get("https://sslproxies.org/")
# driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//th[contains(., 'IP Address')]"))))
# ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 1]")))]
# ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 2]")))]
# driver.quit()
# proxies = []
# for i in range(0, len(ips)):
#     proxies.append(ips[i]+':'+ports[i])
# print(proxies)
# for i in range(0, len(proxies)):
#     try:
#         print("Proxy selected: {}".format(proxies[i]))
#         options = webdriver.ChromeOptions()
#         options.add_argument('--proxy-server={}'.format(proxies[i]))
#         driver = webdriver.Chrome(options=options, executable_path="/Users/hamza/downloads/chromedriver")
#         driver.get("https://www.whatismyip.com/proxy-check/?iref=home")
#         if "Proxy Type" in WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.card-text"))):
#             break
#     except Exception:
#         driver.quit()
# print("Proxy Invoked")


class Scraper:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(executable_path="/Users/hamza/downloads/chromedriver")


class Mediamarkt(Scraper):


    def fillForm(self):
        # driver.get('https://www.mediamarkt.de/checkout/address')
        pass
        driver = self.driver

        zurKasseBtn = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[4]/div[1]/div/div/div/div/div[8]/div/div/div/div/div[4]/div/button'))
        )

        ActionChains(driver).move_to_element(zurKasseBtn).click(zurKasseBtn).perform()
        print("btn clicked")

        time.sleep(1)
        AnmeldungBtn = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'mms-login-form__login-button'))
        )

        ActionChains(driver).move_to_element(AnmeldungBtn).click(AnmeldungBtn).perform()
        print("slept for seconds")

        username = driver.find_element_by_id("mms-login-form__email")
        password = driver.find_element_by_id("mms-login-form__password")
        # fill form and click login btn
        username.send_keys("fatih.cetinkaya.1999@gmail.com")
        password.send_keys("Oecfzqv713844")
        driver.find_element_by_id("mms-login-form__login-button").click()

        def kreditkarte():
            pass
            kreditkarte = driver.find_element_by_xpath(
                "//*[contains(text(), 'Kreditkarte')]"
            )
            return kreditkarte

        visaBtn = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//div[text() = 'Kreditkarte']"))
        )
        print("visa found")
        ActionChains(driver).move_to_element(visaBtn).click(visaBtn).perform()
        weiterBtn = driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[3]/div[1]/div/div[2]/div/div[11]/div/button'
        )

        ActionChains(driver).move_to_element(visaBtn).click(visaBtn).perform()
        ActionChains(driver).click(weiterBtn).perform()

        driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[3]/div[1]/div/div[2]/div/div[8]/div/div/div/div/div[4]/div/button'
        ).click()
        print("script ran well")


    def scrapeMediamarkt(self):
        pass
        url = self.url
        driver = self.driver
        driver.get(url) 

        #COOKIE ACCEPT
        cookieForm = driver.find_element_by_xpath(
            '//*[@id="privacy-layer__wrapper"]/form'
        )
        acceptBtn = driver.find_element_by_css_selector(
            "#privacy-layer-accept-all-button"
        )

        ActionChains(driver).move_to_element(cookieForm).click(acceptBtn).perform()
            
        toCartBtn = False
        while not toCartBtn:
            try:
                

                #/////// WAIT TILL PRODUCT IS AVAILABLE & DETECT ADD TO CART BTN  ////////
                # p = driver.findElement(By.cssSelector("p")).getText()
                # data = driver.find_element_by_tag_name('p')
                # moveToBtn = False
                # while not moveToBtn:
                    # time.sleep(5)
                    
                # moveToBtn = WebDriverWait(driver,1).until(
                #         EC.presence_of_element_located(
                #             (By.ID, 'pdp-add-to-cart-button')
                #         )
                #     )
                merkzettelBtn = driver.find_element_by_css_selector(
                    "#pdp-single-wishlist-button"
                )
                    # print('artikel was not found')
                    # response = requests.get(
                    #     "https://www.mediamarkt.de/de/product/_asus-geforce-rtx%E2%84%A2-3070-tuf-gaming-oc-8gb-90yv0fq6-m0na00-2691247.html",
                    #     proxies={
                    #         "http": "http://26dd8c06bf0a4804ac0458b66c8df1fb:@proxy.crawlera.com:8011/",
                    #     },
                    # )
                print("article is not in stock")
                
                # moveToBtn = driver.find_element_by_css_selector("#pdp-add-to-cart-button")
                # if not merkzettelBtn:
                    

                #     applescript = """
                #     display dialog "Artikel detected! look at your shopping cart" ¬
                #     with title "Detecter" ¬
                #     with icon caution ¬
                #     buttons {"OK"}
                #     """
                #     def macPopup():
                #         subprocess.call("osascript -e '{}'".format(applescript), shell=True)

                #     def windowsPopup():
                #         text = 'Artikel detected! look at your shopping cart'
                #         title = 'Detecter'
                #         ctypes.windll.user32.MessageBoxW(0, text, title, 0x1000)
                        
                #     def articleFound():
                #         ActionChains(driver).move_to_element(moveToBtn).click(moveToBtn).perform()

                #         # wait for modal and basketBtn to show up
                #         WebDriverWait(driver, 3).until(
                #             EC.presence_of_element_located(
                #                 (By.XPATH, '//*[@id="basket"]/div/div[4]/div/button[2]')
                #             )
                #         )
                #         print("located")

                #         # simulate click and add to basket
                #         toWarenkorbBtn = driver.find_element_by_xpath(
                #             '//*[@id="basket"]/div/div[4]/div/button[2]'
                #         )
                #         ActionChains(driver).move_to_element(toWarenkorbBtn).click(
                #             toWarenkorbBtn
                #         ).perform()
                #         print("item added to basket")
                        
                #         self.fillForm() 
                    
                #     p1 = threading.Thread(target=macPopup)
                #     p2 = threading.Thread(target=articleFound)
                #     p1.start()
                #     p2.start()
                #     break
                    
                time.sleep(3)
                driver.refresh()
                

                    # wait for data to be loaded
                    # WebDriverWait(driver, delay).until(
                    #     EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    # )
            except:
                addToCartBtn = driver.find_element_by_css_selector(
                    "#pdp-add-to-cart-button"
                )
                addToCartBtn.click()
                print('Articel found and Btn clicked')
                toCartBtn = True
                # else:
                #     print('esle')
                #     html = driver.page_source
                # # finally:
                # #     driver.quit()
                # #
                # if html:
                #     soup = BeautifulSoup(html, 'lxml')
                #     raw_data = soup.select_one(selector).text
                #     data = json.loads(raw_data)
                # #
                #     import pprint
                #     print(data)


    # makeRequest()
        # scrapeMediamarkt()
