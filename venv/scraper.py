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


def makeRequest():
    url = "https://www.mediamarkt.de/de/product/_koenic-kcm-1019-2576588.html"
    # opts = ChromeOptions()
    # opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path="/Users/hamza/downloads/chromedriver")
    browser = driver

    def fillForm():
        # browser.get('https://www.mediamarkt.de/checkout/address')
        pass
        zurKasseBtn = driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[4]/div[1]/div/div/div/div/div[8]/div/div/div/div/div[4]/div/button'
        )

        ActionChains(browser).move_to_element(zurKasseBtn).click(zurKasseBtn).perform()
        print("btn clicked")

        time.sleep(1)
        AnmeldungBtn = driver.find_element_by_id("mms-login-form__login-button")

        ActionChains(browser).move_to_element(AnmeldungBtn).click(AnmeldungBtn).perform()
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

        visaBtn = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.XPATH, "//div[text() = 'Kreditkarte']"))
        )
        print("visa found")
        ActionChains(browser).move_to_element(visaBtn).click(visaBtn).perform()
        weiterBtn = driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[3]/div[1]/div/div[2]/div/div[11]/div/button'
        )

        ActionChains(browser).move_to_element(visaBtn).click(visaBtn).perform()
        ActionChains(browser).click(weiterBtn).perform()

        driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[3]/div[1]/div/div[2]/div/div[8]/div/div/div/div/div[4]/div/button'
        ).click()
        print("script ran well")


    def scrapeMediamarkt():
        
        pass
        browser.get(url)
        try:
            time.sleep(1)

            cookieForm = driver.find_element_by_xpath(
                '//*[@id="privacy-layer__wrapper"]/form'
            )
            acceptBtn = browser.find_element_by_css_selector(
                "#privacy-layer-accept-all-button"
            )

            ActionChains(browser).move_to_element(cookieForm).click(acceptBtn).perform()

            # p = driver.findElement(By.cssSelector("p")).getText()
            # data = browser.find_element_by_tag_name('p')
            moveToBtn = WebDriverWait(browser,9999999999999999999).until(
                    EC.presence_of_element_located(
                        (By.ID, 'pdp-add-to-cart-button')
                    )
                )
            print('was found')
            
            # moveToBtn = browser.find_element_by_css_selector("#pdp-add-to-cart-button")
            # print('DAAAAAATTAAAAA:',data)
            if moveToBtn:
                import subprocess
                import threading
                import ctypes

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
                    ActionChains(browser).move_to_element(moveToBtn).click(moveToBtn).perform()

                    # wait for modal and basketBtn to show up
                    WebDriverWait(browser, 3).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="basket"]/div/div[4]/div/button[2]')
                        )
                    )
                    print("located")

                    # simulate click and add to basket
                    toWarenkorbBtn = browser.find_element_by_xpath(
                        '//*[@id="basket"]/div/div[4]/div/button[2]'
                    )
                    ActionChains(browser).move_to_element(toWarenkorbBtn).click(
                        toWarenkorbBtn
                    ).perform()
                    print("item added to basket")
                    time.sleep(1)

                    fillForm()    
                def console():
                    print('some long scraping')   
                    time.sleep(30)
                p1 = threading.Thread(target=macPopup)
                p2 = threading.Thread(target=articleFound)

                p1.start()
                p2.start()
                
                

            else:
                print("article is not in stock")

                # wait for data to be loaded
                # WebDriverWait(browser, delay).until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                # )
        except:
            print("some error accured!")
            # else:
            #     print('esle')
            #     html = browser.page_source
            # # finally:
            # #     browser.quit()
            # #
            # if html:
            #     soup = BeautifulSoup(html, 'lxml')
            #     raw_data = soup.select_one(selector).text
            #     data = json.loads(raw_data)
            # #
            #     import pprint
            #     print(data)


    scrapeMediamarkt()

# makeRequest()
    # scrapeMediamarkt()
