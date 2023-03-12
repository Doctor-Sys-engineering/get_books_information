import scrapy


class CwarlBooksInformationSpider(scrapy.Spider):
    name = "cwarl_books_information"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        pass
