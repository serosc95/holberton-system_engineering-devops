#!/usr/bin/python3
"""returns a list containing the titles of all hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    usr = 'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11'
    usrAg = {'User-Agent': usr}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    response = requests.get(url, headers=usrAg)
    json_r = response.json()
    if response.status_code == 200:
        for post in json_r['data']['children']:
            hot_list.append(post['data']['title'])
        new_after = json_r['data']['after']
        if new_after is None:
            return hot_list
        return recurse(subreddit, hot_list, new_after)
    else:
        return None
