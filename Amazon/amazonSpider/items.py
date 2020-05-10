# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # movie_link = scrapy.Field()
    movie_name = scrapy.Field()
    movie_year = scrapy.Field()
    movie_duration = scrapy.Field()
    movie_imagelink = scrapy.Field()

    pass
