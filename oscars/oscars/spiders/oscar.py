from scrapy_playwright.page import PageMethod
import scrapy


class OscarSpider(scrapy.Spider):
    name = "oscar"
    
    def start_requests(self):
        yield scrapy.Request(
            "https://www.scrapethissite.com/pages/ajax-javascript/",
            meta={
                "playwright": True,
                "playwright_include_page": True,
                "playwright_page_methods": [
                    PageMethod("click", "a#2015"),
                    PageMethod("wait_for_selector", "tr.film")
                ]
            }
        )
            
    async def parse(self, response):
        for row in response.css("tr.film"):
            yield {
                "title": row.css("td.film-title::text").get(),
                "awards": row.css("td.film-awards::text").get()
            }

        page = response.meta["playwright_page"]
        page.wait_for_selector("tr.film")

        table = response.css("table")
        print(
            "[TABLE]",
            table.get() if table is not None else "Not Found"
        )

