# -*- coding: utf-8 -*-
import scrapy
import json


class QuotesscrollSpider(scrapy.Spider):
    name = 'QuotesScroll'
    allowed_domains = ['toscrape.com']
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [api_url.format(1)]

    def parse(self, response):
        # parse the response data

        data = json.loads(response.text)

        for quote in data['quotes']:
            yield {
                'author_name': quote['author']['name'],
                'text': quote['text'],
                'tags': quote['tags']
            }
        # check if next_page available

        if data['has_next']:
            next_page = data['page'] + 1
            # generate new req for next page
            yield scrapy.Request(url = self.api_url.format(next_page), callback=self.parse)


