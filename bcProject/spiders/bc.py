# -*- coding: utf-8 -*-
import scrapy
from bcProject.items import BcprojectItem


class BcSpider(scrapy.Spider):
    name = 'bc'
    allowed_domains = ['www.thebetterchinese.com']
    start_urls = ['https://www.thebetterchinese.com/']

    url = 'https://loan.thebetterchinese.com/show/toVipInvest.html?pageNo={}&pageSize=20'
    page = 1

    def start_requests(self):
    	url = self.url.format(self.page)
    	yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        content_div = response.xpath('//div[@class="down_list"]//li')
        for content in content_div[2:]:
        	item = BcprojectItem()
        	title = content.xpath('.//span[1]/text()').extract()
        	item['标题'] = title[0] if title else '暂无标题信息'

        	rate = content.xpath('.//span[2]/text()').extract()
        	item['预期年化利率'] = rate[0] if rate else '暂无预期年化利率信息'

        	term_investment = content.xpath('.//span[3]/text()').extract()
        	item['投资期限'] = term_investment[0] if term_investment else '暂无投资期限信息'

        	Income_method = content.xpath('.//span[4]/text()').extract()
        	item['收益方式'] = Income_method[0] if Income_method else '暂无收益方式信息'

        	money = content.xpath('.//span[5]/text()').extract()
        	item['投资金额'] = money[0] if money else '暂无投资金额信息'

        	Expected_earnings = content.xpath('.//span[6]/text()').extract()
        	item['预期收益'] = Expected_earnings[0] if Expected_earnings else '暂无预期收益信息'

        	operation = content.xpath('.//span[7]/a/text()').extract()
        	item['操作'] = operation[0] if operation else '暂无操作信息'

        	yield item

        	if self.page <= 10:
        		self.page += 1
        		url = self.url.format(self.page)
        		yield scrapy.Request(url, callback=self.parse,dont_filter=True)
