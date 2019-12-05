import scrapy
import json
import pandas as pd

class craigslistScrapy(scrapy.Spider):
	name = "startcraigslistScrapy"
	craigslist_URL = "https://vancouver.craigslist.org/d/cars-trucks/search/cta"
	result = {}
	headers = {
		'user-agent':"Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
		'referer': "https://www.google.com/"
	}
	allowed_domains = ["craigslist.com"]	
	count = 1

	def start_requests(self):
		yield scrapy.Request(self.craigslist_URL, headers = self.headers, callback = self.parse)

	def parse(self, response):
		adInfo = response.css(".result-info")
		
		for element in adInfo:
			adTitle = element.css(".result-title.hdrlnk::text").extract_first()
			adPrice = element.css(".result-price::text").extract_first()
			postingDates = element.css(".result-date::text").extract_first()
			
			self.result[self.count] = {
				"Title":adTitle,
				"Price":adPrice,
				"Date":postingDates
			}
			self.count += 1 

	def close(self, reason):
		if reason == "finished":
			with open ("Cars.json","w") as file:
				json.dump(self.result,file)
			df = pd.read_json("Cars.json")
			df.to_csv("Cars.csv", header = 0)		
	