#!/usr/bin/python3
"""Function to queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyBot/0.0.1"}
    res = requests.get(url, headers=headers)
    if res.status_code == 404:
        return 0
    result = res.json().get("data")
    return result.get("subscribers")
