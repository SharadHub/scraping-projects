# import scrapy
# from my_scraper.items import EbookItem
# from scrapy.loader import ItemLoader

# # class EbookSpider(scrapy.Spider):
# #     name = "ebook"
#     # start_urls = ["https://books.toscrape.com/catalogue/category/books/sequential-art_5"]
    
#     # def __init__(self):
#     #     super().__init__()
#     #     self.page_count = 1
#     #     self.total_pages = 4

#     # def start_requests(self):
#     #     base_url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5"

#     #     while self.page_count <= self.total_pages:
#     #         yield scrapy.Request(
#     #             f"{base_url}/page-{self.page_count}.html"
#     #         )
#     #         self.page_count += 1


#     # def parse(self, response):
#     #     # self.page_count += 1
#     #     print("[PARSE]")
#     #     ebooks = response.css("article.product_pod")

#     #     for ebook in ebooks:
#     #         loader = ItemLoader(item = EbookItem(), selector=ebook)

#     #         loader.add_css("title", "h3 a::attr(title)")
#     #         loader.add_css("price", "p.price_color::text")

#     #         yield loader.load_item()
        
#         # print("[PAGE COUNT]:", self.page_count)

#         # next_btn = response.css("li.next a")

#         # if next_btn:
#         #     next_page = f"{self.start_urls[0]}/{next_btn.attrib['href']}"
#         #     yield scrapy.Request(url=next_page)

# class EbookSpider(scrapy.Spider):
#     name = "ebook"

#     def __init__(self, category="travel_2", *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         print("[CATEGORY]:", category)
#         self.start_urls = [
#             f"https://books.toscrape.com/catalogue/category/books/{category}"
#             ]

#     # def start_requests(self):
#     #     base_url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5"

#     #     while self.page_count <= self.total_pages:
#     #         yield scrapy.Request(
#     #             f"{base_url}/page-{self.page_count}.html"
#     #         )
#     #         self.page_count += 1

#     def parse(self, response):
#         ebooks = response.css("article.product_pod")

#         for ebook in ebooks:
#             url = ebook.css("h3 a").attrib["href"]

#             yield scrapy.Request(
#                 url = self.start_urls[0] + url,
#                 callback=self.parse_details
#             )

#     def parse_details(self, response):
#         main = response.css("div.product_main")

#         loader = ItemLoader(
#             item=EbookItem(),
#             selector=main
#         )

#         loader.add_css("title", "h1::text")
#         loader.add_css("price", "p.price_color::text")

#         stock_status = main.css("p.availability")
#         loader.add_value("quantity", stock_status.re(r'\(.+ available\)'))

#         yield loader.load_item()



import scrapy

class TravelSpider(scrapy.Spider):
    name = "book"
    start_urls = ["https://books.toscrape.com/catalogue/category/books/travel_2"]

    def parse(self, response):
        title = response.css("h3 a").attrib["title"]
        price = response.css("p.price_color::text").get()

        self.log(title)
        self.log(price)