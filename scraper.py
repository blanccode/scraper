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


url = 'https://www.mediamarkt.de/de/product/_siemens-wt45hva1-2671659.html'
driver = webdriver.Chrome(executable_path='/Users/hamza/downloads/chromedriver')
browser = driver

browser.get(url)

    
try:
	time.sleep(1)

	cookieForm = driver.find_element_by_xpath('//*[@id="privacy-layer__wrapper"]/form')
	acceptBtn = browser.find_element_by_css_selector("#privacy-layer-accept-all-button")  
	

	ActionChains(browser).move_to_element(cookieForm).click(acceptBtn).perform()  

	# p = driver.findElement(By.cssSelector("p")).getText()
	# data = browser.find_element_by_tag_name('p')

	moveToBtn = browser.find_element_by_css_selector("#pdp-add-to-cart-button")  
	# print('DAAAAAATTAAAAA:',data)
	if moveToBtn:
		# print(deliveryElement.get_attribute('text'))
		ActionChains(browser).move_to_element(moveToBtn).click(moveToBtn).perform()

		# wait for modal and basketBtn to show up
		WebDriverWait(browser, 3).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="basket"]/div/div[4]/div/button[2]'))
		)
		print('located')

		# simulate click and add to basket
		toWarenkorbBtn = browser.find_element_by_xpath('//*[@id="basket"]/div/div[4]/div/button[2]')
		ActionChains(browser).move_to_element(toWarenkorbBtn).click(toWarenkorbBtn).perform()

	else:
		print('article is not in stock')

        
        # wait for data to be loaded
        # WebDriverWait(browser, delay).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        # )
except:
	print('some error accured!')
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


# proxy = {
#     "https": '134.209.104.116:3128',
#     "http": '134.209.104.116:3128'
# }
# response= requests.get('https://httpbin.org/ip',proxies= proxy)

# print(response.json())
# print(response.text)

