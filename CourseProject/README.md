
## CourseProject 

The whole assignment is written and tested with Sublime, Python 2.7, and used the library of Scrapy and Pandas.


In the linux command console, you can first run:

### scrapy crawl startcraigslistScrapy

then 

### python PandaAnalysis/PandaAnlysis.py


Goal:

The goal is to tie together all the concepts we have and will be learning in this course in to a practical and interesting project. We will be scraping a Craigslist Ad page for information on a topic (Cars, Antiques, Rentals, etc.). We will then store that data and analyze it using our data analysis toolkit and some python skills we’ve learned.

You will be tasked with doing the following:

    1. Pick a URL from a Craigslist search you’d like to scrape ( Eg: https://vancouver.craigslist.org/d/cars-trucks/search/cta )
    2. Create a new Scrapy Project for this course project
    3. Create a new Spider to scrape Craigslist
    4. Design the relevant X-Path Selectors for at least the following: a) Ad Title b) Ad Price c) Posting Date (Please feel free to add more details as you see fit!)
    5. Create a Pandas Dataframe from the selection lists and write them to a CSV file
    6. In a separate python file, read in the CSV and clean the data up a bit if needed (eg. Price)
    7. Plot a histogram (You can adjust the bins) of the data to get a visual of the price distribution

The URL I picked for the project is https://vancouver.craigslist.org/d/cars-trucks/search/cta, the car selling page on Craigslist.

The project is coded with two files, CraigslistScraping.py and PandaAnalysis.py. CraigslistScraping.py uses scrapy module to scrape the Adtitle, AdPrice, Posting Date of the car selling page on Craigslist. Once the information has been scraped by the script, user is allowed to use PandaAnalysis.py under PandaAnalysis folder to see the histogram of price distribution dynamically synchronised with the website once the project is ran. 

*A json file and a csv file are both produced from CraigslistScraping.py containing the same information scraped from the website.
*PandaAnalysis.py is seperated with another folder PandaAnalysis/PandaAnalysis.py, because I found out the file runs prior to CraigslistScraping.py everytime I type scrapy crawl command, which will result into an error initially without the csv file existed.
