import snscrape.modules.twitter as Scraper

for tweet in Scraper.TwitterSearchScraper('from:tesla').get_items():
    print(tweet)
