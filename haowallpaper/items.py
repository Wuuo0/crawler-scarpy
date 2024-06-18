# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dataclasses import dataclass


class PaperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    downloads = scrapy.Field()
    stars = scrapy.Field()
    author = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
