import scrapy


class MigrosspiderItem(scrapy.Item):
    name = scrapy.Field()
    brand = scrapy.Field()
    categories = scrapy.Field()
    unit = scrapy.Field()
    unit_amount = scrapy.Field()
    price = scrapy.Field()
    crm_discount = scrapy.Field()
