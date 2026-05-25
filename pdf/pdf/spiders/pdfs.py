import scrapy


class PdfsSpider(scrapy.Spider):
    name = "pdfs"

    def start_requests(self):
        yield scrapy.Request(
            "https://docs.scrapy.org/en/latest/intro/overview.html",
            meta={
                "playwright": True,
                "playwright_include_page": True
            }
        )


    async def parse(self, response):
        page = response.meta["playwright_page"]
        pdf_bytes = await page.pdf(path="overview.pdf", format="A4")
        await page.close()
