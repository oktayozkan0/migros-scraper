import scrapy


class MigrosSpider(scrapy.Spider):
    name = "migros"
    allowed_domains = ["migros.com"]
    start_urls = ["http://migros.com/"]

    def parse(self, response):
        pass
