#!/usr/bin/python3
"""
    Function queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Retuns the number of total subscribers for a given subreddit"""
    url = "https://www.reddit.com/dev/api/{}/about.json".format(subreddit)
    user_agent = {'User_agent': 'Google Chrome Version 127.0.6533.100'}
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 404:
        return 0
    results = response.json()
    return results.get("data").get("subscribers")
