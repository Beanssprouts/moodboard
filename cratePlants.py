import scrapy
from ..items import ScrapeItem

class CrateplantsSpider(scrapy.Spider):
    name = "cratePlants"
    allowed_domains = ["www.crateandbarrel.com"]
    start_urls = ["https://www.crateandbarrel.com/decorating-and-accessories/artificial-potted-plants-and-trees/1"]

    def parse(self, response):
        items = ScrapeItem()
        
        product_name = response.css('.product-name-text::text').extract()
        price = response.css('.regPrice').css('::text').extract() 

        items['product_name'] = product_name  
        items['price'] = price
        
        yield items
