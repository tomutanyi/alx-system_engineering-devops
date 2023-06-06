#!/usr/bin/python3

"""
Query a subreddit
"""

from requests import get
from sys import argv


headers = {
    "User-Agent": "Of course I had to use a custom User-Agent",
    "X-Forwared-For": "iamthecavalry"
}


def number_of_subscribers(subreddit: str) -> int:
    """
    Query the subreddit
    """
    response = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                   headers=headers)
    data = response.json()
    try:
        if 'error' in data.keys():
            return 0
        else:
            return data['data']['subscribers']
    except Exception as e:
        return 0


if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))
