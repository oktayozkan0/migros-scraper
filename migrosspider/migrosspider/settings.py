BOT_NAME = "migrosspider"

SPIDER_MODULES = ["migrosspider.spiders"]
NEWSPIDER_MODULE = "migrosspider.spiders"


#USER_AGENT = "migrosspider (+http://www.yourdomain.com)"

ROBOTSTXT_OBEY = True

#CONCURRENT_REQUESTS = 32

#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

#COOKIES_ENABLED = False

#TELNETCONSOLE_ENABLED = False

#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

#SPIDER_MIDDLEWARES = {
#    "migrosspider.middlewares.MigrosspiderSpiderMiddleware": 543,
#}


#DOWNLOADER_MIDDLEWARES = {
#    "migrosspider.middlewares.MigrosspiderDownloaderMiddleware": 543,
#}

#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

#ITEM_PIPELINES = {
#    "migrosspider.pipelines.MigrosspiderPipeline": 300,
#}


#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_START_DELAY = 5
#AUTOTHROTTLE_MAX_DELAY = 60
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
#AUTOTHROTTLE_DEBUG = False

#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
