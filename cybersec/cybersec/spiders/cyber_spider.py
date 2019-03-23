import scrapy

file = open("D:/Digital Forensic Engineering/3 th Grade/2 th Period/Access To Information From Web/Search Engine/data_bing.txt","r")
    
file_read = file.readlines()
url_index = file_read[0]
url_real = url_index[0:26]

url = '%s' % url_real


class CyberSpiderClass(scrapy.Spider):
    
    
    name = "cyber"
    
    #start_urls = ['https://thehackernews.com']
    start_urls = [url]
    
    def parse(self,response):
        
        threads = response.xpath("//*[@class='body-post clear']")
        
        for thread in threads:
            
            thread_absolute_link = thread.xpath(".//*[@class='story-link']/@href").extract_first()
            
            yield response.follow(thread_absolute_link,self.parse_thread)
            
    
    def parse_thread(self,response):
        
        contents_div = response.xpath("//div[@dir='ltr']")
        title = response.xpath("//*[@class='story-title']/a/text()").extract()
        date = response.xpath("//div[@class='postmeta']/span/text()").extract()
        author = response.xpath("//div[@class='postmeta']/span/a/text()").extract()
        img_link = response.xpath("//div[@class='separator']/a/@href").extract()
        
        
        
        for content_div in contents_div:
            
            content = (content_div.xpath("//*[@trbidi='on']/text()").extract())
            yield{
                    
                "title": title,"date": date,"author" : author,"content": content,"img_link": img_link
                
                
                    
            }
    
    
    
    