from instapy import InstaPy
from secrets import *

session = InstaPy(username=INSTA_USERNAME, password=INSTA_PASSWORD)
session.login()

session.set_quota_supervisor(
    enabled=True,
    peak_comments_daily=240,
    peak_comments_hourly=21,
    sleep_after=["server_calls_h"],
    sleepyhead=True,
)

session.like_by_tags(["memes", "dank", "tiktok", "coding"], amount=40)
session.set_dont_like(["naked", "nsfw", "dirty"])
session.set_do_follow(True, percentage=70)
session.set_do_comment(True, percentage=70)
session.set_comments(
    [u"This post is 🔥", u"on point 💯", u"I love your posts 😍😍😍", u"true dat😅"]
)
session.end()
