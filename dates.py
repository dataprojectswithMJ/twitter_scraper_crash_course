import snscrape.modules.twitter as Scraper

for tweet in Scraper.TwitterSearchScraper('from:tesla since:2022-10-30 until:2022-11-05').get_items():
    print(tweet)
