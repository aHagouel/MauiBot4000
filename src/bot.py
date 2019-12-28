#!/usr/bin/env python
from __future__ import absolute_import, print_function
import tweepy
import requests as r

# Complete OAuth Authentication
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# initialize API
api = tweepy.API(auth)
print('posting as ' + api.me().name)

#do the stuff
ids = []
media_response = api.media_upload('../media/big-dog.jpg')
ids.append(media_response.media_id_string)
api.update_status('This a MF DAWWWWGGGG', media_ids = ids)

# Upload & tweet image

#api.update_status(status='first bot tweet whattupppp')
