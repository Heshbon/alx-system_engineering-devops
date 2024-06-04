#!/usr/bin/python3
"""The function that query subscribers on a given Reddit subreddit."""


import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if respose.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
