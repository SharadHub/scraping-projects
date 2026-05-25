import scrapy

class LoginSpider(scrapy.Spider):
    name = "login"

    def start_requests(self):
        url = "https://www.scrapethissite.com/pages/advanced/?gotcha=login"


        yield scrapy.FormRequest(
            url=url,
            formdata={
                "email": "bishal@gmail.com",
                "password": "really_strong"
            },
        )
    
    def parse(self, response):
        print(
            "[RESULT]:",
            response.css('div.container div div::text').get()
        )