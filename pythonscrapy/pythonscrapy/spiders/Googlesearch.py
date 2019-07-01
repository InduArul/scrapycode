import scrapy
from ..items import pythonscrapyItem
from googlesearch import search
from bs4 import BeautifulSoup
from scrapy.linkextractors import LinkExtractor

class firsttest(scrapy.Spider):
 
    name="CNA"
              
    def start_requests(self):
        #searchq = open("input.txt","r")
        data = 'Digital Transformation + Channel News Asia'
        for j in search(data, tld= "com", num=10, stop=10, pause=5): 
            print (j)
            urls = [
                    j
                ]   
            for url in urls:
                if 'wikipedia.org' in url:
                    yield scrapy.Request(url, callback=self.parse_no_follow)
                elif '/news/video-on-demand/' in url:
                    yield scrapy.Request(url, callback=self.parse_no_follow) 
                elif '/news/podcasts/' in url:
                    yield scrapy.Request(url, callback=self.parse_no_follow) 
                elif '/video-on-demand/' in url:
                    yield scrapy.Request(url, callback=self.parse_no_follow) 
                elif '/news/videos/' in url:
                    yield scrapy.Request(url, callback=self.parse_no_follow) 
                else:
                    yield scrapy.Request(url=url, callback=self.parse)
    def parse_no_follow(self,response):      
        print("Invalid URL")             
            
    def parse(self,response):
        html = response.text
        soup = BeautifulSoup(html,'lxml')
        items = pythonscrapyItem()
        items['URL'] = response.url
        items['pagetitle']=soup.title.string
        items['articlecreateddate']=response.xpath('//time/text()').get()
        items['PageH1heading'] = response.css('h1::text').extract()
        detailedtext =response.css('p::text').extract() 
        items['Details'] = detailedtext
        #nextpage = LinkExtractor.extract_links(response)
        items['linkurls'] = []
        for link in LinkExtractor(allow=(),deny = ('/news/video-on-demand/','/news/podcasts/'), restrict_xpaths  =('//h2','//h3',)).extract_links(response):
            items['linkurls'].append(link.url)
            yield scrapy.Request(url=link.url, callback=self.parse_items)
        if detailedtext == "":
            print ("no details present")
        else:
            yield items
            
            
    def parse_items(self, response):
        html = response.text
        soup = BeautifulSoup(html,'lxml')
        items = pythonscrapyItem()
        items['URL'] = response.url
        items['pagetitle']=soup.title.string
        items['articlecreateddate']=response.xpath('//time/text()').get()
        items['PageH1heading'] = response.css('h1::text').extract()
        detailedtext =response.css('p::text').extract() 
        items['Details'] = detailedtext
        if detailedtext == "":
            print ("no details present")
        else:
            yield items
        
        
        
        