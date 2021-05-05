from windowPopup import showPopup
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import random
n = random.randint(0,1)

from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

req_proxy = (
    RequestProxy()
)  # you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list()  # this will create proxy list

PROXY = proxies[0].get_address()

opts = Options()

ips = []
for proxy in proxies:
    # if proxy.country == 'Germany':
    ips.append(proxy.get_address())


def refreshCheckItemAvailability(driver, url):
    driver = driver
    url = url
    toCartBtn = False
    while not toCartBtn:
        try:
            refreshLimit = 4
            for x in range(0, 4):

                merkzettelBtn = driver.find_element_by_css_selector(
                    ".detail-error--headline"
                )

                print("article is not in stock stock.")
                time.sleep(2)
                driver.refresh()

            driver.quit()
            rotateIp(url)

        except:
            addToCartBtn = driver.find_element_by_css_selector(".is--large")
            # addToCartBtn.click()
            print("Articel found and Btn clicked")

            showPopup()

            toCartBtn = True


def refreshCheckItemAvailabilityAlternate(driver, url):
    driver = driver
    url = url
    toCartBtn = False
    while not toCartBtn:
        try:
            refreshLimit = 4
            for x in range(0, 4):

                merkzettelBtn = driver.find_element_by_css_selector(
                    "#product-top-right .font-weight-bold"
                )

                print("article is not in stock stock.")
                time.sleep(2)
                driver.refresh()

            driver.quit()
            rotateIpForAlternate(url)

        except:
            addToCartBtn = driver.find_element_by_css_selector("#add-to-cart-form .tp-button")
            # addToCartBtn.click()
            print("Articel found and Btn clicked")

            showPopup()

            toCartBtn = True


def rotateIpForAlternate(url):
    print("rotating ip")
    user_agent = (
        "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
    )

    for ip in ips:

        time.sleep(2)
        webdriver.DesiredCapabilities.CHROME["proxy"] = {
            "httpProxy": ip,
            "ftpProxy": ip,
            "sslProxy": ip,
            "proxyType": "MANUAL",
        }

        webdriver.DesiredCapabilities.CHROME["acceptSslCerts"] = True

        if n == 0:
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36"

        opts.add_argument("user-agent=" + user_agent)

        # print(webdriver.DesiredCapabilities.CHROME)
        driver = webdriver.Chrome(
            executable_path="/Users/hamza/downloads/chromedriver", options=opts
        )
        driver.get(url)

        # driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
        # print(driver.execute_script("return navigator.userAgent;"))
        # # Setting user agent as Chrome/83.0.4103.53
        # driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

        user_agent_check = driver.execute_script("return navigator.userAgent;")
        print(user_agent_check)
        time.sleep(1)

        refreshCheckItemAvailabilityAlternate(driver, url)

        # merkBtn = WebDriverWait(driver, 99).until(
        #         EC.presence_of_element_located((By.ID, 'pdp-single-wishlist-button'))
        #     )
        # time.sleep(2)
        # driver.quit()