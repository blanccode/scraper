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

url = "http://httpbin.org/ip"

proxy = '207.244.241.139:8080'
try:

    r = requests.get('https://google.com', proxies={'http': proxy, 'https': proxy})
    print(r.json())

except:
    print('failed')


# import scrapy
# from ..items import TestscrapyItem


# class TestspiderSpider(scrapy.Spider):
#     name = 'testspider'

#     def start_requests(self):
#         start_urls = 'https://www.saturn.de/de/product/_asus-geforce-rtx%E2%84%A2-3080-tuf-gaming-oc-10gb-90yv0fb1-m0nm00-2681861.html'
#         headers = {
#             'Connection': 'keep-alive',
#             'Cache-Control': 'max-age=0',
#             'DNT': '1',
#             'Upgrade-Insecure-Requests': '1',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
#             'Sec-Fetch-User': '?1',
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#             'Sec-Fetch-Site': 'same-origin',
#             'Sec-Fetch-Mode': 'navigate',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'Accept-Language': 'en-US,en;q=0.9',
#         }
#         yield scrapy.Request(start_urls)

        

#     def parse(self, response):
#         # item = TestscrapyItem()

#         # warenkorbBtn = response.css('#pdp-add-to-cart-button').extract()

#         # items['warenkorbBtn'] = warenkorbBtn
        
#         # yield items
#         print('hi')
   
