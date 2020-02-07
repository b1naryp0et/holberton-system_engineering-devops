#!/usr/bin/python3
""" Function which queries reddit api for number of subscribers """

import requests
from sys import argv

def number_of_subscribers(subreddit):

    url = 'https://reddit.com/r/' + subreddit + '/about/.json'
    usr_agnt = {'User-agent': 'Mozilla/5.0'}
    x = requests.get(url, allow_redirects=False, headers=usr_agnt)
    
    try:
        return(x.json().get('data').get('subscribers'))
    except:
        return 0
