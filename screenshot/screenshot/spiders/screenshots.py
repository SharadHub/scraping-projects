from scrapy_playwright.page import PageMethod
import scrapy

class ScreenshotsSpider(scrapy.Spider):
    name = "screenshot"
    
    def start_requests(self):
        yield scrapy.Request(
            "https://quotes.toscrape.com/scroll",
            meta={
                "playwright": True,
                "playwright_include_page": True,
            }
        )
            
    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.screenshot(path="oscar.png")

        await page.close()