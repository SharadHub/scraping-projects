import scrapy
import json


class ApiendpointsSpider(scrapy.Spider):
    name = "points"
    start_urls = ["https://dummyjson.com/products"]

    def parse(self, response):
        print(
            "[PRINT]"
        )
        data = json.loads(response.body)

        products = data["products"]

        for product in products:
            clean_data = {
                "title": product["title"],
                "price": product["price"],
                "category": product["category"],
                "rating": product["rating"],
                "stock": product["stock"],
                "brand": product.get("brand")
            }
            yield clean_data
