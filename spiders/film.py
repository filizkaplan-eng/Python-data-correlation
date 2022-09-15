# -*- coding: utf-8 -*-
import scrapy


class FilmSpider(scrapy.Spider):
    name = 'film'
    allowed_domains = ['trendyol.com']
    custom_settings = {
            'FEED_URI': 'veriler.csv',
            'FEED_FORMAT': 'csv'
                    }

    def start_requests(self):
        url='https://www.trendyol.com/cep-telefonu?siralama=4&pi=10'
            
        yield scrapy.Request(url)

    def parse(self, response):

        degerlendirme=response.xpath('.//span[@class="ratingCount"]/text()').extract()
        kargo = response.xpath('.//div[@class="stmp fc"]/text()').extract()
        fiyat=response.xpath('.//div[@class="prc-box-sllng"]/text()').extract()

        yield {'değerlendirme':degerlendirme ,'fiyat':fiyat, 'kargo_durumu': kargo}




















        """
        #&pi=4
            #https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu-aksesuarlari/cep-telefonu-kulaklik?srt=SALES_VOLUME&vt=catalogView
            #'https://yemek.com/tarif/'
            #'https://www.fullhdfilmizlesene.com/en-cok-izlenen-filmler/2'
            #'https://www.fullhdfilmizlesene.com/en-cok-izlenenler'
        
        
        
        
        td=response.xpath('.//span[@class="trz-td"]/text()').extract()
        tda=response.xpath('.//span[@class="trz-tda"]/text()').extract()
        tr = response.xpath('.//span[@class="trz-tr"]/text()').extract()
        korku= response.xpath('.//a[@title="Korku Film izle"]/text()').extract()
        aksiyon = response.xpath('.//a[@title="Aksiyon Film izle"]/text()').extract()
        aile = response.xpath('.//a[@title="Aile Film izle"]/text()').extract()
        fantastik = response.xpath('.//a[@title="Fantastik Filmler izle"]/text()').extract()
        savas = response.xpath('.//a[@title="Savaş Film izle"]/text()').extract()
        animasyon = response.xpath('.//a[@title="Animasyon Filmler izle"]/text()').extract()
        blu = response.xpath('.//a[@title="Blu Ray Filmler izle"]/text()').extract()
        komedi = response.xpath('.//a[@title="Komedi Film izle"]/text()').extract()
        bilimk = response.xpath('.//a[@title="Bilim Kurgu Film izle"]/text()').extract()
        yerli = response.xpath('.//a[@title="Yerli Filmler izle"]/text()').extract()
        romantik = response.xpath('.//a[@title="Romantik Filmler izle"]/text()').extract()
        yield {'td': td ,'tda':tda , 'tr':tr,'korku':korku,'aksiyon':aksiyon, 'aile':aile, 'fantastik':fantastik,'savas':savas,'animasyon':animasyon, 'blu':blu, 'komedi':komedi,'bilimk':bilimk,'yerli':yerli,'romantik':romantik}"""

