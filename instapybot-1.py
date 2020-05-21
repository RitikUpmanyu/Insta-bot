
from instapy import InstaPy
from secrets import *

session = InstaPy(username=INSTA_USERNAME, password=INSTA_PASSWORD)
session.login()
session.like_by_tags(["code", "coding", "developer"], amount=5)