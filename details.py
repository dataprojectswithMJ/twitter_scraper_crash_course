import snscrape.modules.twitter as Scraper
import pandas as pd

tweet_list=[]
for i,tweet in enumerate(Scraper.TwitterSearchScraper('from:tesla').get_items()):
    if i > 9:
        break
    tweet_list.append([tweet.user.username, tweet.user.verified, tweet.user.followersCount, tweet.content, tweet.date])

df= pd.DataFrame(tweet_list, columns=['Username','Is Verified','Followers Count','Tweet','Date'])
df.to_csv('Tesla_Scrape.csv')