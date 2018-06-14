# -*- coding: utf-8 -*-

# Scrapy settings for baidubaike project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'baidubaike'

SPIDER_MODULES = ['baidubaike.spiders']
NEWSPIDER_MODULE = 'baidubaike.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'baidubaike (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
    'Accept': '* / *',
    'Accept - Encoding': 'gzip, deflate, br',
    'Accept - Language': 'zh - CN, zh;',
    'q': '0.9',
    'Connection': 'keep - alive',
    # 'Cookie':'BAIDUID=A85C76144D36B1EC67C144817FB9C1BF:FG=1; BID=DF578F53C8206802C4DAA0B8DADFA8F1:FG=1; HUM=; HUN=; newloc=%7C%7C; toptips=0; BDTUJIAID=d1e4fedc757ff35c848fd961a5626a52; kuaixun=1; hz=73; __bsi=12504819107804070407_00_6_R_N_3_0303_c02f_Y',
    # 'Cookie': 'BAIDUID=03FDB08473F462E2130FE25C73EE6BA4:FG=1; BIDUPSID=03FDB08473F462E2130FE25C73EE6BA4; PSTM=1527151522; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=26522_1441_21123_18560_26430; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1527587928,1527588338,1527646476,1527647772; PSINO=2; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1527648464',
    'Cookie': 'BAIDUID=9E66AA422E3487E7728B790543E67E05:FG=1; BIDUPSID=9E66AA422E3487E7728B790543E67E05; PSTM=1527939527; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-92%3A; H_PS_PSSID=1453_21087_26350; BKWPF=3; BDSFRCVID=4p0sJeCCxG3A4kr7QnRaHc7EGiH0zO5mg2WE3J; H_BDCLCKID_SF=tRk8oIDatKvbfP0kb-r_bn0_hM4X5-RLfbnjoPOF5lOTJh0RLjOOK6-uhR5KBPtf3mv0aIJLBK5VeIo5Qjbke4tX-NFtt6_OtM5; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1528214336,1528254550,1528254600,1528257235; PSINO=1; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1528267984; pgv_pvi=1067592704; pgv_si=s3261998080',
    'Host': 'baike.baidu.com',
    'Referer': 'https://baike.baidu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'baidubaike.middlewares.BaidubaikeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'baidubaike.middlewares.BaidubaikeDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'baidubaike.pipelines.BaidubaikePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
