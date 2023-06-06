#!/usr/bin/python3

"""
query the Reddit
"""

from requests import get
from sys import argv


def top_ten(subreddit: str) -> None:
    """
    function
    """
    headers = {
        "User-Agent": "Marvel",
        "X-Forwared-For": "Phil"
    }

    request_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        response = get(request_url, headers=headers,
                       allow_redirects=False).json()
        data = response['data']['children']
        [print(post['data']['title']) for post in data[:10]]
    except Exception:
        print("None")

