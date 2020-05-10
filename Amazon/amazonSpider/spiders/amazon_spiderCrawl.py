# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonspiderItem


class AmazonSpidercrawlSpider(scrapy.Spider):
    name = 'amazon_spiderCrawl'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/-/es/gp/browse.html?node=2649512011&ref_=nav_em_0_2_29_2__nav_desktop_sa_intl_movies'
        , 'https://www.amazon.com/s?i=movies-tv&bbn=2921749011&rh=n%3A2625373011%2Cn%3A%212901003011%2Cn%3A%212901007011%2Cn%3A2921749011%2Cn%3A2649512011&language=es&rw_html_to_wsrp=1&ref=Movies_H1_deals'
        ]

    custom_settings = {
        'FEED_FORMAT' : 'json',
        'FEED_URI' : 'file:C://Users//mirivera//Documents//MIRIVERA//Applied Data Science Master//Data Acquisition & Preparation//VisualStudio//webScrapping//Amazon//Peliculas&TV-%(time)s.json'
    }

    def parse(self, response):
        
        for movie in response.css(".s-item-container"):
            yield {
                'movie_name' : movie.css('.s-access-title::text').extract(),
                'movie_year' : movie.css('.a-letter-space~ .a-letter-space+ .a-color-secondary').css('::text').extract(),
                'movie_duration' : movie.css('#result_5 .a-fixed-left-grid+ .a-fixed-left-grid .a-color-secondary , .a-fixed-left-grid~ .a-fixed-left-grid+ .a-fixed-left-grid .a-color-secondary').css('::text').extract(),
                'movie_imagelink' : movie.css('.cfMarker::attr(src)').extract()
            }
    