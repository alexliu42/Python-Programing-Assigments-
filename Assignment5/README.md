
## Assignment 5 

The whole assignment is written and tested with Sublime, Python 3.6, and used the library of scrapy.


In the linux command console, you can run:

### scrapy crawl startMovieScrapy



Goal:

The goal of this assignment is to utilize on what we learned in all our classes so far to build a small application for ourselves. We are going to scrape our local cinema listings for movie titles, then use imdb to search for ones that have a rating above a certain threshold every time we run our script (eg. Weekly). The script can be improved, built upon and automated further to run as a job on your system and have it email or text you the results at the end of each week!

You will need to start by installing scrapy on your system as Spyder does not include the framework:

1. Open the Anaconda Prompt and type: pip install scrapy
2. [Optional] To install Twilio for text/email you can do: pip install twilio

Now, you will need to create a scrapy project from the command line. Navigate to the folder you want to start your project in in the Anaconda Prompt (using cd to change directory and either dir for Windows or ls for Mac/Linux to see the files in each directory). Once you’re in the folder, you can:

1. Start creating the scaffolding, by typing: scrapy startproject MovieScraper
2. Then navigate (cd) to the spider folder by typing: cd MovieScraper, and then: cd  spiders
3. Inside this folder, you can create your MovieScraper.py file (which you can edit in Spyder)
4. * When you are ready to run your spider, in this spiders folder on the Anaconda Prompt, you can type: scrapy crawl name_of_your_spider where the name is what you have as the “name” attribute in your python file for your spider.

Next, inside your spider file, make sure to give it the following attributes at the top of the class after you’ve imported scrapy and made a class MovieScraper of type scrapy.Spider:

1. name – A string to allow us to use the scrapy crawl command to refer to this spider
2. start_urls – A list of urls to start scraping, in this case just one URL: https://www.cinemaclock.com/movies/in-theatres
3. allowed_domains – A list of domain names we can scrape: [“cinemaclock.com”, “imdb.com”]
4. MIN_RATING – A floating point of the minimum imdb rating we want for a “good” movie. ie. 7.5
5. good_movies – Either a list or a dictionary to store the movies that have a higher than min_rating
6. imdb_url – This will be to search each movie. We just need to concatenate the title of the movie we scraped after the url: ttps://www.imdb.com/earcsh/title/?title=   


Finally, these two functions will make it easier to do this assignment:

1. def start_requests(self, response) – This will be where the spider starts it’s crawling. You can start scraping the cinemaclock site here and yielding to your callback a scrapy.Request(imdb_search_url + movie_title, callback=self.scrape_imdb) object. In this example I’ll call the callback: scrape_imdb. *Put this yield in a loop for each movie name you scrape from response.css.
2. def scrape_imdb(self, response) – This will take each imdb search page and try to find the rating. It will then store that movie if it meets our rating criteria.
3. def closed(self, reason) – Here we can write our good_movies to a file or send a text/email when the reason == “finished”



The assignment is coded with scrapy module. I implement the global variables on top of the class for the usages of start_requests, parse, parse2 and close functions. Start_rquests yields the cinemaclock website for parse function to look for the movie titles in our local cinema, concatenate the title of the movie with the imdb_url, and yield the response from imdb webstie. If the movie title is not found in imdb webstie, then the terminal will show the error message between comparnig nonetype to str, but continue for my other asynchronous good movies search. In parse2 function, I scrape the movies that have higher ratings than our MIN_RATING 7.4 from imdb website. Lastly,I format the scraped movies in a dictionary and save it as a json file. The json file is named "Good_Movies.json" which is stored at Assignment5/MovieScraper/MovieScraper/spider/ 

The obstacle I am meeting is that I don't know how to combine my parse2 function with my first for-loop in parse function. This results me into writing another for loop in parse2 in order to prevent for overwriting my saved data in the dictionary. 


*I did not see the backpage of the assignment until I am pushing my code. Since I am running out of my time for term project and final, so I didn't do the challenge. However, I assume the task of visiting RottenTomatoes will be a similar process as what I did in the assignment. For example: create another parse function for RottenTomatoes to scrape the information we want.
