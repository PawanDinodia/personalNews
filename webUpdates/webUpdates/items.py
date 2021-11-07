# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebupdatesItem(scrapy.Item):
    # define the fields for your item here like:
    updateId = scrapy.Field()
    updateUrl = scrapy.Field()
    updateSubUrl = scrapy.Field()
    updateCatagory = scrapy.Field()
    updateCatagoryTitle = scrapy.Field()
    updateTitle = scrapy.Field()
    updateFound = scrapy.Field()
    updateDates = scrapy.Field()
    updateSubCatagory = scrapy.Field()
    updateLink = scrapy.Field()
    markNew = scrapy.Field()
    setImportant = scrapy.Field()