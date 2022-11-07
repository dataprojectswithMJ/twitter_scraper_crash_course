import snscrape.modules.twitter as Scraper

for i,tweet in enumerate(Scraper.TwitterSearchScraper().get_items()):
    if i > 999999:
        break
    print(f'Tweet no {i}. Tweet by {tweet.user.username}\n {tweet.sourceLabel}')
