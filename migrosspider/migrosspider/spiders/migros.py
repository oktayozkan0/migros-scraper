import scrapy
from ..items import MigrosspiderItem


class MigrosSpider(scrapy.Spider):
    name = "migros"

    @staticmethod
    def child_extractor(data: dict):
        l = []
        excluded_ids = [20000000072311, 20000000072310]
        for category in data:
            if category["data"]["id"] in excluded_ids:
                continue
            def extract(c: dict):
                if not c["children"]:
                    l.append(c["data"]["prettyName"])
                else:
                    for i in c["children"]:
                        extract(i)
            extract(category)
        return l

    def start_requests(self):
        yield scrapy.Request("https://www.migros.com.tr/rest/categories", callback=self.get_categories)

    def get_categories(self, response):
        c = response.json()
        categories = c["data"]
        child_categories = self.child_extractor(categories)

        for category in child_categories:
            yield scrapy.Request(f"https://www.migros.com.tr/rest/search/screens/{category}?sayfa=1", callback=self.paging_if_necessary)

    def paging_if_necessary(self, response):
        data = response.json()
        self.parse(response=response)
        page_count = data["data"]["searchInfo"]["pageCount"]

        if page_count > 1:
            for i in range(2, page_count+1):
                category = data["data"]["searchInfo"]["categoryAggregations"][0]["prettyName"]
                yield scrapy.Request(f"https://www.migros.com.tr/rest/search/screens/{category}?sayfa={i}", callback=self.parse)

    def parse(self, response):
        data = response.json()
        for i in data["data"]["searchInfo"]["storeProductInfos"]:
            item = MigrosspiderItem()
            item["name"] = i["name"]
            item["brand"] = i["brand"]["name"]
            item["categories"] = [j["label"] for j in data["data"]["metaInfo"]["breadcrumbs"]]
            item["unit"] = i["unit"]
            item["unit_amount"] = i["unitAmount"]
            item["price"] = i["shownPrice"]/100
            try:
                item["crm_discount"] = i["properties"]["CRM_DISCOUNT"]["CRM_DISCOUNT"]
            except:
                item["crm_discount"] = None
            yield item
