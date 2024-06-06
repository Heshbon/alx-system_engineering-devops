#!/usr/bin/python3
"""The function to query subscribers on a given Reddit subreddit."""


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    import requests

    sub_details = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "My-User-Custom"},
        allow_redirects=False
    )
    if sub_details.status_code >= 300:
        return 0

    return sub_details.json().get("data").get("subscribers")
