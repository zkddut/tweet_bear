import tweepy
import json

def tweetTextPhoto(message, photo):
  with open('twitter_auth.json') as file:
    secrets = json.load(file)

  auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
  auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

  twitter = tweepy.API(auth)

  if photo is None:
    twitter.update_status(message)
  else:
    twitter.update_with_media(photo, message)

