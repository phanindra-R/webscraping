import scrapy
import pickle
from ..items import FlipcartScrapyItem

class myspider(scrapy.Spider):
	page_plus = 2
	name = 'spidy'
	start_urls = [
		'https://www.flipkart.com/search?q=laptops&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&as-searchtext=laptops&page=1'
	]
	
	def parse(self, response):
		items  = FlipcartScrapyItem()
		box = response.css('div.bhgxx2.col-12-12')
		for entries in box :
			title = entries.css('div._3wU53n::text').extract()
			rating = entries.css('div.hGSR34::text').extract()
			price = entries.css('div._1vC4OE._2rQ-NK::text').extract()

			items['title'] = title
			items['rating'] = rating
			items['price'] = price

			yield  items
		
		next_page = 'https://www.flipkart.com/search?q=laptops&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&as-searchtext=laptops&page=" + str(myspider.page_plus) + "'
		if myspider.page_plus <= 11:
			myspider.page_plus +=1
			yield response.follow(next_page,callback = self.parse) 	

