from windowPopup import showPopup


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


def rotateIp(url):
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

        refreshCheckItemAvailability(driver, url)

        # merkBtn = WebDriverWait(driver, 99).until(
        #         EC.presence_of_element_located((By.ID, 'pdp-single-wishlist-button'))
        #     )
        # time.sleep(2)
        # driver.quit()