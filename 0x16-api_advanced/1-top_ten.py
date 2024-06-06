#!/usr/bin/python3
"""The function to print hot posts on a given Reddit subreddit."""


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    import requests

    sub_details = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "My-User-Custom"},
        allow_redirects=False
    )
    if sub_details.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in sub_details.json().get("data").get("children")]
