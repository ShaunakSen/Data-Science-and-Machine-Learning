# -*- coding: utf-8 -*-
import scrapy


class AuthorsspiderSpider(scrapy.Spider):
    name = 'AuthorsSpider'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        author_urls = response.css('div.quote > span > a::attr(href)').extract()
         
        for author_url in author_urls:
            url = response.urljoin(author_url)
            # create a request to the url with a separate callback
            print ("Author URL...", url)
            yield scrapy.Request(url = url, callback=self.parse_details)
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        next_page_url = response.urljoin(next_page_url)
        print ("Next url:", next_page_url)    
        if next_page_url:
            yield scrapy.Request(url = next_page_url, callback=self.parse)    

    def parse_details(self, response):
        # extract data from author
        yield {
            'name':response.css('h3.author-title::text').extract_first().strip(),
            'birthdate': response.css('span.author-born-date::text').extract_first().strip()
        }
