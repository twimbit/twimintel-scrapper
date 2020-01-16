import scrapy
from ..items import FragrancesItem


class FragSpider(scrapy.Spider):
    name = 'frags'
    start_urls = [
        "https://www.mychemist.com.au/shop-online/601/fragrances-womens?size=120&sort=abc&page=1",  # change to 120
        "https://www.mychemist.com.au/shop-online/600/fragrances-mens?size=120&sort=abc&page=1"  # change to 120
    ]
    size = 120  # change to 120
    men_pages = 6  # Total number of men pages
    women_pages = 10  # Total number of women pages

    men_page_number = 2  # constant, do not change
    women_page_number = 2  # constant, do not change
    items = FragrancesItem()

    def parse(self, response):
        product_no = 1
        Products = response.css(
            'a.product-container').xpath("@href").extract()

        while product_no <= FragSpider.size:
            # FragSpider.items['Product'] = Products[product_no - 1]
            product_no += 1
            yield response.follow(Products[product_no - 2], callback=self.parse_details)

        if FragSpider.men_page_number <= FragSpider.men_pages:
            next_page_men = 'https://www.mychemist.com.au/shop-online/600/fragrances-mens?size=120&sort=abc&page=' + \
                str(FragSpider.men_page_number)
            FragSpider.men_page_number += 1
            yield response.follow(next_page_men, callback=self.parse)
        if FragSpider.women_page_number <= FragSpider.women_pages:
            next_page_women = 'https://www.mychemist.com.au/shop-online/601/fragrances-womens?size=120&sort=abc&page=' + \
                str(FragSpider.women_page_number)
            FragSpider.women_page_number += 1
            yield response.follow(next_page_women, callback=self.parse)

    def parse_details(self, response):

        High_in_Demand_Status = response.css(
            'div.shipping_time_indicator:nth-of-type(8)').attrib['style']

        product_link = response.xpath(
            '//*[@id="head"]/link[21]/@href').get()

        Total_Price = response.css(
            'div.retailPrice::text').extract()[0].strip()

        Discount = response.css('div.Savings::text').extract()[0].strip()

        Current_Price = response.css(
            'div.Price div+ span::text').extract()[0].strip()

        Product_Name = response.css('h1::text').extract()[0].strip()

        Low_Stock_Parent = response.css('div:nth-of-type(10)').attrib['style']

        Low_Stock_Child_1 = response.css(
            'div:nth-of-type(10) div.Add2Cart:nth-of-type(1)').attrib['style']

        Low_Stock_Child_2 = response.css(
            'div:nth-of-type(10) div.Add2Cart:nth-of-type(2)').attrib['style']

        Out_of_Stock_Parent = response.css(
            'div:nth-of-type(11)').attrib['style']

        Out_of_Stock_Child_1 = response.css(
            'div:nth-of-type(11) div.Add2Cart:nth-of-type(1)').attrib['style']

        Out_of_Stock_Child_2 = response.css(
            'div:nth-of-type(11) div.Add2Cart:nth-of-type(2)').attrib['style']

        Product_id = response.css('div.product-id::text').extract()[0].strip()

        Frag_For = response.css('#curr_cat_id::text').extract()[0].strip()

        FragSpider.items['product_link'] = product_link
        FragSpider.items['High_in_Demand_Status'] = High_in_Demand_Status
        FragSpider.items['Total_Price'] = Total_Price
        FragSpider.items['Discount'] = Discount
        FragSpider.items['Current_Price'] = Current_Price
        FragSpider.items['Product_Name'] = Product_Name
        FragSpider.items['Low_Stock_Parent'] = Low_Stock_Parent
        FragSpider.items['Low_Stock_Child_1'] = Low_Stock_Child_1
        FragSpider.items['Low_Stock_Child_2'] = Low_Stock_Child_2
        FragSpider.items['Out_of_Stock_Parent'] = Out_of_Stock_Parent
        FragSpider.items['Out_of_Stock_Child_1'] = Out_of_Stock_Child_1
        FragSpider.items['Out_of_Stock_Child_2'] = Out_of_Stock_Child_2
        FragSpider.items['Product_id'] = Product_id
        FragSpider.items['Frag_For'] = Frag_For

        yield FragSpider.items
