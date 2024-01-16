#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an
invalid subreddit is given, the function should return 0."""

import json
import requests

def number_of_subscribers(subreddit):
    """Return the number subscribers"""
    URL = "https://www.reddit.com/r/{}/about/.json". format(subreddit)
    header = {'User-Agent': 'Chrome/51.0.2704.103'}
    r= requests.get(URL, headers=headers)
    if r.status_code == 200:
        r= r.json()
        return r['data']['subscribers']
    else:
        return 0
