#!/usr/bin/python3
""" reddit api """

import requests


def recurse(subreddit, hot_list=[], after=''):
    """ Reddit api """
