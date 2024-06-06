#!/usr/bin/python3
"""The function that queries subscribers on a given Reddit subreddit."""

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    import requests

    res = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "My-User-Custom"},
        allow_redirects=False
    )
    if res.status_code >= 300:
        return 0

    return res.json().get("data", {}).get("subscribers", 0)

