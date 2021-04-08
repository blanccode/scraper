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
import subprocess
import threading
import ctypes

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


        try:
          

            cookieForm = driver.find_element_by_xpath(
                '//*[@id="privacy-layer__wrapper"]/form'
                
            )
            print('something')

            acceptBtn = driver.find_element_by_css_selector(
                "#privacy-layer-accept-all-button"
            )

            ActionChains(driver).move_to_element(cookieForm).click(acceptBtn).perform()

            # p = driver.findElement(By.cssSelector("p")).getText()
            # data = driver.find_element_by_tag_name('p')
            moveToBtn = WebDriverWait(driver,9999999999999999999).until(
                    EC.presence_of_element_located(
                        (By.ID, 'pdp-add-to-cart-button')
                    )
                )
            print('was found')
            
            # moveToBtn = driver.find_element_by_css_selector("#pdp-add-to-cart-button")
            if moveToBtn:
                

                applescript = """
                display dialog "Artikel detected! look at your shopping cart" ¬
                with title "Detecter" ¬
                with icon caution ¬
                buttons {"OK"}
                """
                def macPopup():
                    subprocess.call("osascript -e '{}'".format(applescript), shell=True)

                def windowsPopup():
                    text = 'Artikel detected! look at your shopping cart'
                    title = 'Detecter'
                    ctypes.windll.user32.MessageBoxW(0, text, title, 0x1000)
                    
                def articleFound():
                    ActionChains(driver).move_to_element(moveToBtn).click(moveToBtn).perform()

                    # wait for modal and basketBtn to show up
                    WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="basket"]/div/div[4]/div/button[2]')
                        )
                    )
                    print("located")

                    # simulate click and add to basket
                    toWarenkorbBtn = driver.find_element_by_xpath(
                        '//*[@id="basket"]/div/div[4]/div/button[2]'
                    )
                    ActionChains(driver).move_to_element(toWarenkorbBtn).click(
                        toWarenkorbBtn
                    ).perform()
                    print("item added to basket")
                    
                    self.fillForm() 

                
                p1 = threading.Thread(target=macPopup)
                p2 = threading.Thread(target=articleFound)

                p1.start()
                p2.start()
                

            else:
                print("article is not in stock")

                # wait for data to be loaded
                # WebDriverWait(driver, delay).until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                # )
        except:
            print("some error accured!")
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
