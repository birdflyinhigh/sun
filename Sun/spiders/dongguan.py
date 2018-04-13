# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Sun.items import SunItem


class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    # 提取列表页的url

    rules = (
        Rule(LinkExtractor(allow=r'index.php/question/questionType'), follow=True),
        Rule(LinkExtractor(allow=r'html/question/\d+/\d+.shtml'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        item = SunItem()

        item['number'] = response.xpath('/html/body/div[6]/div/div[1]/div[1]/strong/text()').extract_first().split(':')[-1].strip()
        item['url'] = response.url
        item['title'] = response.xpath('/html/head/title/text()').extract_first().split('_')[0]
        item['content'] = response.xpath('/html/head/meta[@name="description"]/@content').extract_first()

        yield item



