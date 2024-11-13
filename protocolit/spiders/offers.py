import scrapy


class OffersSpider(scrapy.Spider):
    name = "offers"
    allowed_domains = ["theprotocol.it"]
    start_urls = ["https://theprotocol.it/filtry/python?kw=python+developer"]

    def parse(self, response):
        pass
