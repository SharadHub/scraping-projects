import scrapy
from scrapy.crawler import CrawlerProcess

class TravelSpider(scrapy.Spider):
    name = "travel"
    start_urls = ["https://books.toscrape.com/catalogue/category/books/travel_2"]

    def parse(self, response):
        title = response.css("h3 a").attrib["title"]
        price = response.css("p.price_color::text").get()

        print("[TITLE]:", title)
        print("[PRICE]:", price)


crawler = CrawlerProcess()
crawler.crawl(TravelSpider)

crawler.start()