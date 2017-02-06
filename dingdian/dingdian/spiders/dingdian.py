import re
import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from ..items import DingdianItem


class Myspider(scrapy.Spider):
    name="dingdian"
    allow_domains=['23us.com']
    bash_url="http://www.23us.com/class/"

    bashurl=".html"

    def start_requests(self):
        for i in range(1,11):
            url=self.bash_url+str(i)+'_1'+self.bashurl
            
            yield Request(url,self.parse)
    
    def parse(self,response):        
        max_num = response.xpath('//*[@id="pagelink"]/a[14]/text()').extract()[0]
        base_url=str(response.url)[:-7]
        for number in range(1,3):
            url=base_url+"_"+str(number)+self.bashurl

            yield Request(url,callback=self.get_name)

    def get_name(self,response):
        text=response.text
        item = DingdianItem()
        item['name']=text
        return item
        
