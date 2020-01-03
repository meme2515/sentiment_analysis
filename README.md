# 👨‍💼 Trump's Twitter Account

In this project I have analyzed Donald Trump's Tweets to find insights such as the upload time distribution across different devices, change in device usage over time, and [VADER](https://github.com/cjhutto/vaderSentiment) sentiment score of tweets containing specific words (such as nytimes and fox news). The project is divided into three distinct parts.

## 1. Data Import 🦜

First I have constructed a pandas dataframe of Trump's Tweets provided in .json format. The information contained in the resulting dataframe are time of upload, device used, tweet content, and retweet count. The unique identifier of each Tweet is as provided by Twitter.

## 2. Tweet Source 📱

I found a total of 10 unique sources for Tweets including iPhone, Android, and Web Client. First, I compared the distribution of tweets uploaded via iPhone vs. Android from year 2016 to 2019 and found that Android usage was heavier in the first two years but was almost completely replaced by iPhone in the last two years (Trump switched from Android to iPhone some time in 2017, according to [this Verge article](https://www.theverge.com/2017/3/29/15103504/donald-trump-iphone-using-switched-android)).

It was also observed that before 2017, Trump's use of Android peaked in hours where he's not in work whereas his use of iPhone peaked in work hours. This supports the existing hypothesis that his Android tweets were written personally whereas his iPhone tweets were written by his staff during this time.

## 3. Sentiment Score 😄

To quantify the sentiment of specific Tweets, I have used the VADER (Valence Aware Dictionary and sEntiment Reasoner) lexicon to translate specific words to sentiment scores. VADER is a sentiment analysis tool that is specifically attuned to sentiments expressed in social media. 

Here's an example of one of the most negative Tweets by Trump:

> the rigged russian witch hunt goes on and on as the “originators and founders” of this scam continue to be fired and demoted for their corrupt and illegal activity. all credibility is gone from this terrible hoax, and much more will be lost as it proceeds. no collusion!

An example of one of the most postive Tweets:

> thank you to all of my great supporters, really big progress being made. other countries wanting to fix crazy trade deals. economy is roaring. supreme court pick getting great reviews. new poll says trump, at over 90%, is the most popular republican in history of the party. wow!
