#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyBot/0.0.1"}
    params = {'limit': 10}
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 404:
        print("None")
        return
    result = res.json().get("data")
    for title in result.get("children"):
        print(title.get("data").get("title"))
