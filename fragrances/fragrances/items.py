# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


# Extracted Data -> Temporary containers (items) -> Storing in database
import scrapy


class FragrancesItem(scrapy.Item):
    product_link = scrapy.Field()
    High_in_Demand_Status = scrapy.Field()
    Total_Price = scrapy.Field()
    Discount = scrapy.Field()
    Current_Price = scrapy.Field()
    Product_Name = scrapy.Field()
    Low_Stock_Parent = scrapy.Field()
    Low_Stock_Child_1 = scrapy.Field()
    Low_Stock_Child_2 = scrapy.Field()
    Out_of_Stock_Parent = scrapy.Field()
    Out_of_Stock_Child_1 = scrapy.Field()
    Out_of_Stock_Child_2 = scrapy.Field()
    Product_id = scrapy.Field()
    Frag_For = scrapy.Field()
