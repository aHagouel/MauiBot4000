#!/usr/bin/env python
from __future__ import absolute_import, print_function
from gpiozero import MotionSensor
from datetime import datetime 
import tweepy
import requests as r
import os, sys, subprocess

#TODO: Add console output.

# Complete OAuth Authentication for Twitter Bot

# <<insert auth keys!>> TODO: Put your keys into a file and read so this is generic

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# initialize API
api = tweepy.API(auth)
print('posting as ' + api.me().name)

#TODO: Refactor into an actual program instead of this terrible script.
def tweet_picture(f):
    ids = []
    media_response = api.media_upload(f)
    ids.append(media_response.media_id_string)
    api.update_status('WOOF!', media_ids = ids)

# Motion Sensor loop
pir = MotionSensor(4)
filepath = '/home/pi/Development/MauiBot4000/media/img'
while True:
    pir.wait_for_motion()
    print('Motion Detected')
    print('Taking a picture of the sucker!')
    #TODO: simplify by having BASH output the location of the file.
    now = datetime.now().strftime("%Y-%m-%d:%T")
    os.system('./webcam.sh ' + now)
    picture_path = filepath + now + '.jpg'
    tweet_picture(picture_path)
    pir.wait_for_no_motion()
    print('No motion detected')
    