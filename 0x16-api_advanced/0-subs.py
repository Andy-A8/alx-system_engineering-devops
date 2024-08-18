#!/usr/bin/python3
"""
    Function queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Retuns the number of total subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User_Agent': 'Chrome/127.0.6533.100'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
