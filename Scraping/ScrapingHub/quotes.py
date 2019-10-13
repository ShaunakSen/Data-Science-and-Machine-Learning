# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    # urls that we want our spider to visit
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        # callback method
        quotes = response.css('div.quote')
        for quote in quotes:
            item = {
                'author_name': quote.css('small.author::text').extract_first(),
                'text': quote.css('span.text::text').extract_first(),
                'tags': quote.css('a.tag::text').extract()
            }
            yield item

        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        next_page_url = response.urljoin(next_page_url)
        print ("Next url:", next_page_url)    
        if next_page_url:
            # create new request
            print ("Here")
            yield scrapy.Request(url = next_page_url, callback=self.parse)    
        else:
            print ("Next url is ", next_page_url)    
            


