import os
import tweepy
import pandas
import configparser

config = configparser.ConfigParser()
config.read("config")
api_key = config['TWITTER']['SECRET_KEY']
print(api_key)