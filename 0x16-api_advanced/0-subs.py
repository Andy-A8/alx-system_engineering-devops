#!/usr/bin/python3
"""
    Queries the Reddit API and returns the number of subscribers
    for a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.

    If not a valid subreddit, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {'User-agent': 'Google Chrome Version 125.0.6422.113'}
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    result = response.json().get('data)
