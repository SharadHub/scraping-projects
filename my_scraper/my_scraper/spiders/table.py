import scrapy
from my_scraper.items import EbookItem
from scrapy.loader import ItemLoader

class TableSpider(scrapy.Spider):
    name = "table"
    start_urls = ["https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"]

    def parse(self, response):
        print(
            "THIS" \
            "WILL" \
            "PARSE" \
            "TABLE" \
            "CONTENT" \
            "OF THIS" \
            "WEBPAGE"
        )
        table = response.css("table")

        product_details = {}

        for row in table.css("tr"):
            heading = row.css("th::text").get()
            data = row.css("td::text").get()

            product_details[heading] = data

            yield product_details


{'UPC': 'a22124811bfa8350', 
 'Product Type': 'Books', 
 'Price (excl. tax)': '£45.17', 
 'Price (incl. tax)': '£45.17', 
 'Tax': '£0.00', 'Availability': 
 'In stock (19 available)', 
 'Number of reviews': '0'}