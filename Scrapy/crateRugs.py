import scrapy
from ..items import ScrapeItem


class CraterugsSpider(scrapy.Spider):
    name = "crateRugs"
    allowed_domains = ["www.crateandbarrel.com"]
    start_urls = ["https://www.crateandbarrel.com/rugs/wool-rugs/1"]

    def parse(self, response):
        items = ScrapeItem()
        
        product_name = response.css('.product-name-text::text').extract()
        price = response.css('.regPrice').css('::text').extract() 

        items['product_name'] = product_name  
        items['price'] = price
        
        yield items
