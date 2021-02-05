#!/usr/bin/python3
"""returns a list containing the titles of all hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyBot/0.0.1"}
    params = {"after": after}
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 404:
        return None
    json_r = res.json().get("data")
    for post in json_r['data']['children']:
        hot_list.append(post['data']['title'])
    new_after = json_r['data']['after']
    if new_after is None:
        return hot_list
    return recurse(subreddit, hot_list, new_after)
