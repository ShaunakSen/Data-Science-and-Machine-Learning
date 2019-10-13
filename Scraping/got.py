# Link: https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/

# A crawler is a program that browses web sites and downloads content. 
# Sometimes crawlers are also referred as spiders.

# List of things that need to be extracted:

# Title of each post
# Number of votes it has
# Number of comments
# Time of post creation

# response.css(".imors3-0").extract()
# response.css(".imors3-0").extract_first()
# response.css(".imors3-0::text").extract()
# response.css("._1rZYMD_4xY3gRcSS3p8ODO").extract()
# selecting multiple classes
# response.css(".score.unvoted").extract_first()


# Note: Scrapy has two functions to extract the content extract() and extract_first().

# The .attr(attributename) is used to get the value of the specified attribute of the matching element.

# response.css("time::attr(title)").extract()


