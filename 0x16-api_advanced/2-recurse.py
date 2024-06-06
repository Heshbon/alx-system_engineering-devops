#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""


import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"count": count, "after": after}
    headers = {"User-Agent": "My-User-Custom"}
    sub_details = requests.get(
        url,
        params=params,
        headers=headers,
        allow_redirects=False
    )

    if sub_details.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in sub_details.json()
                        .get("data")
                        .get("children")]

    info = sub_details.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))
