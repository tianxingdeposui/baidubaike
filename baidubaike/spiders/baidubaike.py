# -*- coding: utf-8 -*-
import scrapy
# import requests
import json
from baidubaike.items import BaidubaikeItem
class BaidubaikeSpider(scrapy.Spider):
    name = "baidubaike"
    allowed_domains = ["baidubaike.com"]
    start_urls = []

    # for i in range(1,10):
    #     url = 'http://baike.baidu.com/view/' + str(i) + '.htm'
    #     html = requests.get(url, headers=header, allow_redirects=False)
    #     item = html.headers['Location']
    #     geturl = 'https://baike.baidu.com' + str(item)
    for page in range(1,10):
        start_url = 'http://baike.baidu.com/view/' + str(page) + '.htm'
        start_urls.append(start_url)
    start_urls = start_urls
    print(start_urls)
    # def start_requests(self):
    #     for page in range(1,10):
    #         i = 'http://baike.baidu.com/view/' + str(page) + '.htm'
    # url = 'http://baike.baidu.com/view/'
    # # offset = 1
    # for offset in range(1,1000):
    #     start_urls = [url + str(offset) + '.htm']
    # start_urls = start_urls

    def parse(self, response):
        # items = []
        item = BaidubaikeItem()
        name = response.xpath('//h1//text()').extract()[0]
        summary = response.xpath('//div[@class="lemma-summary"]//text()').extract()
        summary = ''.join(''.join(summary).split())
        content = response.xpath('//div[@class="main-content"]//div[@class="para-title level-2"]//text() | //div[@class="main-content"]//div[@class="para"]//text()').extract()
        content = ''.join(''.join(content).split())

        # baidubaikeidlink = response.xpath('//dd[@class="description//@href').extract()[0]
        baidubaikeidlink = response.xpath('//dd[@class="description"]//li[2]//@href').extract()[0]
        baidubaikeid = baidubaikeidlink.replace('/historylist/', '').split('/')[1]
        baidubaikeid_url = 'https://baike.baidu.com/api/wikiui/sharecounter?lemmaId=' + str(baidubaikeid) + '&method=get'
        print(baidubaikeid_url)

        edits = response.xpath('//dd[@class="description"]//li[2]//text()').extract()[0]
        edits = edits.replace('编辑次数：', '').replace('次', '').split()
        editCount = edits[0]
        print(editCount)

        # body = response.body.decode('utf-8')
        # html = body
        # print(html)

        scripts = response.xpath('//script//text()').extract()
        for script in scripts:
            if 'newLemmaIdEnc' in script:
                pvid = script.split('newLemmaIdEnc:')[1].split('}')[0].strip().replace('"', '')
                print(pvid)
                pvurl = 'https://baike.baidu.com/api/lemmapv?id=' + str(pvid)
        print(pvurl)

        tags = response.xpath('//dd[@id="open-tag-item"]//text()').extract()
        tags = ''.join(''.join(tags).split())

        starrelationlist = []
        starrelations = response.xpath('//div[@class="star-info-block relations"]//ul[@class="slider maqueeCanvas"]/li')
        for number in range(0, len(starrelations)):
            starrelationsname = starrelations[number].xpath('.//text()')
            starrelationslink = starrelations[number].xpath('.//a//@href')
            starrelationsimg = starrelations[number].xpath('.//img/@src')
            starrelationsname = ''.join(''.join(starrelationsname).split())
            starrelationslink = 'https://baike.baidu.com' + ''.join(''.join(starrelationslink).split())
            starrelationsimg = ''.join(''.join(starrelationsimg).split())
            starrelation = starrelationsname + '-' + starrelationslink + '-' + starrelationsimg
            starrelationlist.append(starrelation)
        print(starrelationlist)

        basicinfos = []
        basicinfonames = response.xpath('//div[@class="basic-info cmn-clearfix"]//dt[@class="basicInfo-item name"]')
        basicinfovalues = response.xpath('//div[@class="basic-info cmn-clearfix"]//dd[@class="basicInfo-item value"]')
        for i in range(0, len(basicinfonames)):
            basicinfoname = basicinfonames[i].xpath('.//text()').extract()
            basicinfovalue = basicinfovalues[i].xpath('.//text()').extract()
            basicinfoname = '\1' + ''.join(''.join(basicinfoname).split())
            basicinfovalue = '\2' + ''.join(''.join(basicinfovalue).split())

            basicinfo = basicinfoname + basicinfovalue
            basicinfos.append(basicinfo)
        basicinfos = ''.join(basicinfos)
        print(basicinfos)

        item['name'] = name
        item['summary'] = summary
        item['content'] = content
        item['url'] = response.url
        item['basicinfo'] = basicinfos
        item['tags'] = tags
        item['starrelationlist'] = starrelationlist
        item['editCount'] = editCount
        item['pvurl'] = pvurl
        # item['html'] = body
        # print(item)
        # items.append(item)
        # yield item
        # yield scrapy.Request(pvurl,callback=self.parse02,dont_filter=True)
        yield scrapy.Request(baidubaikeid_url,meta={'meta1': item},callback=self.parse01,dont_filter=True)
        # if self.offset < 10000:
        #         #     self.offset = self.offset + 1
        #         # yield scrapy.Request(self.url + str(self.offset) + '.htm', callback=self.parse)
    #def parse_page(self,response):
    def parse01(self,response):
        meta1 = response.meta['meta1']
        item = BaidubaikeItem()
        body = response.body
        body = json.loads(body)
        print(body)
        shareCount = body['shareCount']
        likeCount = body['likeCount']
        item['name'] = meta1['name']
        item['summary'] = meta1['summary']
        item['content'] = meta1['content']
        item['url'] = meta1['url']
        item['basicinfo'] = meta1['basicinfo']
        item['tags'] = meta1['tags']
        item['starrelationlist'] = meta1['starrelationlist']
        item['editCount'] = meta1['editCount']
        item['shareCount'] = shareCount
        item['likeCount'] = likeCount
        item['pvurl'] = meta1['pvurl']
        # item['html'] = meta1['html']
        pvurl = meta1['pvurl']
        yield scrapy.Request(pvurl,meta={'meta2': item},callback=self.parse02,dont_filter=True)
    def parse02(self,response):
        meta2 = response.meta['meta2']
        print('pvurl :',response.url)
        item = BaidubaikeItem()
        body = response.body
        body = json.loads(body)
        pv = body['pv']
        print(pv)
        item['name'] = meta2['name']
        item['summary'] = meta2['summary']
        item['content'] = meta2['content']
        item['url'] = meta2['url']
        item['basicinfo'] = meta2['basicinfo']
        item['tags'] = meta2['tags']
        item['starrelationlist'] = meta2['starrelationlist']
        item['editCount'] = meta2['editCount']
        item['shareCount'] = meta2['shareCount']
        item['likeCount'] = meta2['likeCount']
        item['pvurl'] = meta2['pvurl']
        item['pv'] = pv
        # item['html'] = meta2['html']
        yield item