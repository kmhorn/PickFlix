#!/usr/bin/env python

import praw
import random

reddit = praw.Reddit(client_id='dJjmxch1qusesA', client_secret='vLRMvTU3Rg4tbwOkGuXhLyXeM7Q', user_agent='PickFlix script by /u/PickFlix')

usa_list = []
for sub in reddit.subreddit('NetflixBestOf').top('week'):
    if "[US]" in sub.title:
        usa_list.append(sub.title)

print(random.choice(usa_list)).split("]")[1]
