# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'Login'
    login_url = 'http://quotes.toscrape.com/login'
    start_urls = [login_url]

    def parse(self, response):
        # get csrf token
        token = response.css('input[name = "csrf_token"]::attr(value)').extract_first()
        print ("CSRF TOKEN IS...", token)
        # create dict with data we want to send to server

        data = {
            'csrf_token': token,
            'username': 'shaunak1105',
            'password': 'abcd'
        }

        # submit a POST request

        yield scrapy.FormRequest(url = self.login_url, formdata = data, callback = self.parse_quotes)

    def parse_quotes(self, response):
        # parse the page after spider is logged in

        # for each quote
            # extract the goodreads link of the author

            for quote in response.css("div.quote"):
                yield {
                    'author_name': quote.css("small.author::text").extract_first(),
                    'author_url': quote.css('small.author ~ a[href*="goodreads.com"]::attr(href)').extract_first()
                }
