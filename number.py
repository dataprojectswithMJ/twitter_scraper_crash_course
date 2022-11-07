import snscrape.modules.twitter as Scraper

for i,tweet in enumerate(Scraper.TwitterSearchScraper('tesla').get_items()):
    if i > 9:
        break
    print(f'Number {i} \n Tweet:{tweet}')