import scrapy
from ..items import ScrapeItem

class ElmchairsSpider(scrapy.Spider):
    name = "elmChairs"
    start_urls = [
        "https://www.westelm.com/shop/furniture/living-room-chairs/?cm_type=gnav&originsc=furniture&tabnav=non-mobiletabnav"
                  
                  ]

    def parse(self, response):
        items = ScrapeItem()
        
        product_name = response.css('.product-name::text').extract()
        price = response.css('.amount').css('::text').extract() 

        items['product_name'] = product_name  
        items['price'] = price
        
        yield items