#!/usr/bin/python3
"""The function that queries subscribers on a given Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Custom"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return 0

    data = res.json().get("data", {})
    return data.get("subscribers", 0)
