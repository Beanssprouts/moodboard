import scrapy
from ..items import ScrapeItem


class CratesofasSpider(scrapy.Spider):
    name = "crateSofas"
    start_urls = ["https://www.crateandbarrel.com/furniture/sofas/1"]

    def parse(self, response):
        items = ScrapeItem()
        
        product_name = response.css('.product-name-text::text').extract()
        price = response.css('.regPrice').css('::text').extract() 

        items['product_name'] = product_name  
        items['price'] = price
        
        yield items