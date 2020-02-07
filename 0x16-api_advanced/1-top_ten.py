#!/usr/bin/python3
""" Module which queries reddit api """

import requests


def top_ten(subreddit):
    """ Lists first 10 hot posts in given subreddit """

    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    usr_agnt = {'User-agent': 'Mozilla/5.0'}
