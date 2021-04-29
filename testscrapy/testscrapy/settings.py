import scraper_helper as sh

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = sh.get_dict (
'''
accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7
cookie: __cfduid=dfb9ef39e6ff53a36ee2cfc96dae47a8c1618057883; optid=5b44ded7-02a9-4a9e-a1e2-d97943778988; s_id=31029fc7-6e82-47a7-908c-8ee76e9fedb7; MC_PS_SESSION_ID=31029fc7-6e82-47a7-908c-8ee76e9fedb7; p_id=31029fc7-6e82-47a7-908c-8ee76e9fedb7; MC_PS_USER_ID=31029fc7-6e82-47a7-908c-8ee76e9fedb7; t_fpd=true; CONSENTMGR=c1:0%7Cc2:0%7Cc3:0%7Cc4:0%7Cc5:0%7Cc6:0%7Cc7:0%7Cc8:0%7Cc9:0%7Cc10:0%7Cc11:0%7Cc12:0%7Cc13:0%7Cc14:0%7Cc15:0%7Cts:1618057893645%7Cconsent:false; optid=5b44ded7-02a9-4a9e-a1e2-d97943778988; MC_GDPR_COOKIE=|f=1|c=0|a=0|m=0|; __cf_bm=be46b715147b455b318b813229658aa65925246a-1619574151-1800-AbpQMnabXMW63YmDD+RwjpnkHE/QdfmK9DToF+RdGgBXY/qxypb0dowkqmaWiD6FzzlRlh1nvcej3xdg4UJwxM+o4Rts5+P8e/p3ZVAGAr7+; ts_id=490dd123-e91a-42c3-88ca-366b84f14a29; _msbps=72; __cfruid=cfe503f78dfce1bcf1329f6d77d1b2500b0c9c0b-1619574152; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiJiMTY5MWZmOS02OTNkLTQ3YjAtODQ4Yy1hNTFjNjQ4ZmU4NzEiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjE5NTc0MTUyLCJleHAiOjE2MjA3ODM3NTIsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.AO-BqX4Fs5Ff3-EFpjb58SlMkWb8baKYbMKrQ29b76d7-sip-6u6qZ9_QD7D-O9p1hQpSOvLEQm8EofjfA_Ggd0xY_pgTDOQJAcaWYYEh7SBA5_O-3eAqXT0cd50_nguskTCMjI_eSd-O_zrx7Mbpw0L_BGmZRnYk0fUxRMRBgdSIJMqSmUNFMVLIA8y1OQ05CFvAqacALE8udk84ZFtQDjT6kBrLJ_KSBf1xPbogQVP-uQOan3uIjuKhEMnIr1HS8-2jYo86aFtpsdryoQD9uWElNA1k_41GOqlN4sgU5VxNR-oQW0NJFZ_WKYe9l4WAFE-gMu99qgfeHl5eohfpQ; r=VQaXAmOzrU4MeJpPdq5FHLfTpol48zvHiyMIdjzhdcRRoyjkYfsnMzn3m7z5JopD; utag_main=v_id:017916245dcd00204a7472ea162803078007007000b7e$_sn:1$_se:3$_ss:0$_st:1619576100231$ses_id:1619574152654%3Bexp-session$_pn:3%3Bexp-session
referer: https://www.saturn.de/de/product/_asus-geforce-rtx%E2%84%A2-3080-tuf-gaming-oc-10gb-90yv0fb1-m0nm00-2681861.html
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
sec-ch-ua-mobile: ?0
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36
'''
)

# Scrapy settings for testscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'testscrapy'

SPIDER_MODULES = ['testscrapy.spiders']
NEWSPIDER_MODULE = 'testscrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'testscrapy (+http://www.yourdomain.com)'
# USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False



# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'testscrapy.middlewares.TestscrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'testscrapy.middlewares.TestscrapyDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'testscrapy.pipelines.TestscrapyPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
