import scrapy
from scrapy.selector import Selector

class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = "https://quotes.toscrape.com/"

    async def parse(self, response):
        page = response.meta["playwright_page"]

        title = await page.title()

        await page.fill("input[name=username]", "random")
        await page.fill("input[name=password]", "random")
        await page.click("input[type=submit]")

        html_content = await page.inner_html("body")

        await page.close()

        body = Selector(text=html_content)


        yield{
            "heading": body.css("h1::text").get(),
            "paragraph": body.css("p::text").get()
        }

