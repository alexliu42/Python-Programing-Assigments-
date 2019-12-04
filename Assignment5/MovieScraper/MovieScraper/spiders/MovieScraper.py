import scrapy
import json

class MoiveScraper(scrapy.Spider):
	name='startMovieScrapy'
	start_urls =["https://www.cinemaclock.com/movies/in-theatres"]
	allowed_domains = ["cinemaclock.com", "imdb.com"]
	MIN_RATING = 7.4
	good_movies = {}
	imdb_url = ["https://www.imdb.com/search/title?title="]

	headers = {
		'user-agent':"Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
		'referer': "https://www.google.com/"
	}
	count = 1

	
	def start_requests(self):
		yield scrapy.Request(self.start_urls[0], headers=self.headers, callback=self.parse)
			
	def parse(self, response):
		movieTitles = response.css(".movietitle > a::text").getall()
		for title in movieTitles:	
			searchURL = self.imdb_url[0] + title
			yield scrapy.Request(searchURL, headers=self.headers, callback=self.parse2)
		
	def parse2(self, response):
		imdbTitle = response.css(".lister-item-header > a ::text").get()
		imdbRating = response.css("div").xpath("@data-value").get()
		if (imdbRating > str(self.MIN_RATING)):
			while imdbTitle != None:
				self.good_movies[self.count] = {
					'Title':imdbTitle,
					'Rating':imdbRating
				}
				self.count += 1
				imdbTitle = None
	
	def close(self, reason):
		if reason == "finished":
			with open ("Good_Movies.json", "w") as file:
				json.dump(self.good_movies,file)
			print("\nA json file of good rating movies is generated!\n")




		
