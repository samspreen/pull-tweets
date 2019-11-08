#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 23:00:46 2019

@author: samspreen
"""


# https://pypi.org/project/GetOldTweets3/

import GetOldTweets3 as got
import numpy as np
import pandas as pd


combdf = pd.DataFrame() 




# The code below pulls all the tweets and stores them in var = tweet

tweetCriteria = got.manager.TweetCriteria().setUsername("SouthwestAir")\
                                           .setSince("2017-04-01")\        # First date inclusive
                                           .setUntil("2017-05-01")\        # Second date exclusive
                                           .setMaxTweets(0)

tweet = got.manager.TweetManager.getTweets(tweetCriteria)



#The code below creates a dataframe and exports to csv

ids = []
permalinks = []
usernames = []
tos = []
dates = []
retweets = []
favorites = []
mentions = []
hashtags = []
geos = []
text = []

for i in tweet:
    user_id = i.id
    ids.append(user_id)  #this is actually the tweet ID
    
    plink = i.permalink
    permalinks.append(plink)
    
    uname = i.username
    usernames.append(uname)
    
    to = i.to  #who its being tweeted at
    tos.append(to)
    
    date = i.date #this is in UTC
    dates.append(date)
    
    rts = i.retweets #number of retweets
    retweets.append(rts)
    
    favs = i.favorites  #number of favorites
    favorites.append(favs)
    
    ment = i.mentions  #users mentioned (#?)
    mentions.append(ment)
     
    tags = i.hashtags  #hashtags (not sure if # or the actual tag itself)
    hashtags.append(tags)
    
    geo = i.geo        #location hasnt come up in any yet 
    geos.append(geo)
    
    string = i.text   #text of the tweet
    text.append(string)
    
df = {'user id':ids, 'permalink':permalinks, 'username':usernames, 'to':tos, "date":dates, 'retweets':retweets, "favorites":favorites, "mentions":mentions,
      'hashtags':hashtags, "geo":geos, "text":text}

df = pd.DataFrame(df)

combdf = pd.concat([df,combdf])  #combine the dataframes

len(combdf['date'])


#combdf.to_csv('SW_apr.csv', sep = ",")

