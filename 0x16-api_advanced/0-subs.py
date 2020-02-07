#!/usr/bin/python3
""" Module  to query reddit api for number of subscribers """

import requests

def number_of_subscribers(subreddit):
    """ Function which queries reddit api for number of subscribers """


    url = 'https://reddit.com/r/' + subreddit + '/about/.json'
    usr_agnt = {'User-agent': 'Mozilla/5.0'}
    x = requests.get(url, allow_redirects=False, headers=usr_agnt)
    
    try:
        return(x.json().get('data').get('subscribers'))
    except:
        return 0
