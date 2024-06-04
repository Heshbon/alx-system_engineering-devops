#!/usr/bin/python3
"""The function that query subscribers on a given Reddit subreddit."""


import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except (KeyError, ValueError):
            return 0
    else:
        return 0

