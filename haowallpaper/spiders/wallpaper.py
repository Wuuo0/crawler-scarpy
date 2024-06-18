import scrapy
from scrapy import Request
from ..items import PaperItem


class WallpaperSpider(scrapy.Spider):
    name = "wallpaper"
    allowed_domains = ["haowallpaper.com"]

    # start_urls = ["https://haowallpaper.com"]
    def start_requests(self):
        home = "https://haowallpaper.com/homeView?page="
        for page in range(1, 4):
            url = home + str(page)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        # block = response.xpath('//*[@id="contentDiv"]/div/div/div[1]/div')
        cards = response.css('div.card')
        for card in cards:
            item = PaperItem()
            link = card.css('a::attr(href)').get()
            item['link'] = link
            url = 'https://haowallpaper.com' + link
            yield Request(url, callback=self.parse_page, cb_kwargs={'item': item})

    def parse_page(self, response, **kwargs):
        item = kwargs['item']
        downloads = response.css('div.col-4-son-1 div.col-son-ico')[4].css('span::text').get()
        stars = response.css('div.col-4-son-1 div.col-son-ico')[5].css('span::text').get()
        author = response.css('span.user-nick-name::text').get()
        image_urls = response.css('img#imgLoad::attr(src)').getall()
        # self.log(f'url: {image_urls}')
        item['author'] = author
        item['downloads'] = downloads
        item['stars'] = stars
        item['image_urls'] = image_urls
        return item
