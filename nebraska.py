import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://egov.uscis.gov/cris/processingTimesDisplay.do' +
        '?serviceCenter=992&displaySCProcTimes=Service+Center+Processing+DatesName',
    ]

    def start_requests(self):
        print '---------------------------'
        for u in self.start_urls:
            yield scrapy.Request(u, cookies={'_ga': 'GA1.2.1480389112.1494473824',
                                             '_ceg.s': 'oprrds',
                                             '_ceg.u': 'oprrds', 
                                             'fsr.s': '{"v2":1,"v1":1,"rid":"de358f9-93825418-83c7-4299-5bd23","cp":{"delivery_src":"none","Homepage":"Y"},"to":4,"c":"https://www.uscis.gov/","pv":1,"lc":{"d14":{"v":1,"s":false}},"cd":14,"sd":14,"mid":"de358f9-93825797-a96b-06c0-c269f","rt":false,"rc":false,"f":1494473826108}',
                                             'JSESSIONID' : 'abco23gPX6wEu-QNJx4Vv',
                                             '__utma': '34570677.667791996.1492934418.1495165052.1495303539.6',
                                             '__utmc': '34570677',
                                             '__utmz': '34570677.1492934418.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'},
                                headers={'Accept-Encoding' : 'gzip, deflate, sdch, br', 
                                        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh-TW;q=0.4',
                                        'Upgrade-Insecure-Requests': '1',
                                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36', 
                                        'Accept': 'text/html,application/xhtml+xml,application/xml',
                                        'q': '0.9,image/webp,*/*;q=0.8',
                                        'Cache-Control': 'max-age=0'})




    def parse(self, response):
        raw = response.xpath("//tbody[@title='I-485']//tr[@class='first']//td//text()").extract()[-1]
        processed_date = re.sub('\s+', '', raw)
        
        if(processed_date == 'July2,2016'):
            print 'OKay, it\'s still July 2, 2016'
        else:
            print 'It\'s changed'
            #send email to me
            self.sendEmail(processed_date)
        
    def sendEmail(self, new_date):
        pass



        