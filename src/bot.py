#!/usr/bin/env python
from __future__ import absolute_import, print_function
import tweepy
import requests as r

# Complete OAuth Authentication
consumer_key='FAGMW0DPsGmWu7RdX6IY3UId5'
consumer_secret='54gD4KMBd7ZBM5hkwOUR22VSyWuYZ8848ppZA0L42dPZCjwfaB'
access_token='3940138797-TIaeaFGfqDeEdpL9NVDpRn6GCjJ7OSpehfG0GLh'
access_token_secret='7KIOAgBnEVPOxS9rh2k7eRMFXvBCqjQ6ipXMl64i1OYSG'
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
