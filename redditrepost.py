import sys
import praw  # pip install praw
import time
import urllib
import random
from InstagramAPI import InstagramAPI  # pip install InstagramApi
from autopost import upload
from secrets import *

"""-------------------------------------------------------- Reddit API setup -----------------------------------------------------------------------------"""

reddit_p = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent=user_agent,
    username=shell_door,
)

sr_memes = reddit_p.subreddit("IndianMemeTemplates")
sr_dankmemes = reddit_p.subreddit("dankmemes")
sr_bpt = reddit_p.subreddit("desimemes")

"""------------------------------------------------------- Variables used for checking or lists -----------------------------------------------------------------------------"""

submissionnum_memes = 0
submissionnum_dankmemes = 0
submissionnum_bpt = 0
bpt_urls = []
dankmemes_urls = []
meme_urls = []
bpt_dict = {}
bpt_count = 1
meme_dict = {}
meme_count = 1
dankmeme_count = 1
dankmeme_dict = {}
"""------------------------------------------------------ Loop that indexes urls to lists -------------------------------------------------------------------------------"""

for submission_bpt in sr_bpt.hot(limit=15):
    if ".jpg" in submission_bpt.url and "redd" in submission_bpt.url:
        bpt_urls.insert(submissionnum_bpt, submission_bpt.url)
        submissionnum_bpt + 1
        bpt_dict[submission_bpt.url] = bpt_count
        bpt_count = bpt_count + 1
    else:
        continue

for submission_meme in sr_memes.hot(limit=15):
    if ".jpg" in submission_meme.url and "redd" in submission_meme.url:
        meme_urls.insert(submissionnum_memes, submission_meme.url)
        submissionnum_memes + 1
        meme_dict[submission_meme.url] = meme_count
        meme_count = meme_count + 1
    else:
        continue

for submission_dankmeme in sr_dankmemes.hot(limit=10):
    if ".jpg" in submission_dankmeme.url and "redd" in submission_dankmeme.url:
        dankmemes_urls.insert(submissionnum_dankmemes, submission_dankmeme.url)
        submissionnum_dankmemes + 1
        dankmeme_dict[submission_dankmeme.url] = dankmeme_count
        dankmeme_count = dankmeme_count + 1
    else:
        continue

"""----------------------------------------------------------- Loop that iterates through each url and saves them --------------------------------------------------------------------------"""

for i_meme, image_meme in enumerate(meme_urls, start=1):
    urllib.request.urlretrieve(image_meme, r"YOUR DIR" + str(i_meme) + ".jpg")
    time.sleep(2.5)

time.sleep(5)

for i_bpt, image_bpt in enumerate(bpt_urls, start=1):

    urllib.request.urlretrieve(image_bpt, r"YOUR DIR" + str(i_bpt) + ".jpg")
    time.sleep(2.5)

time.sleep(5)

for i_dankmeme, image_dankmeme in enumerate(dankmemes_urls, start=1):
    urllib.request.urlretrieve(image_dankmeme, r"YOUR DIR" + str(i_dankmeme) + ".jpg")
    time.sleep(2.5)

"""--------------------------------------------------------- Lists of hastags, caption phrases, and meme index for deciding which meme-type to pull from ----------------------------------------------------------------------------"""

caption_phrases = [
    "Wowzers",
    "thats gonna be a big yikes from me dawg",
    "how ya guys like this one?",
    "these are all prerecorded messages",
    "im definitely not a robot",
    "we will enslave the humans eventually",
    "my python dont",
    "coming up with captins is hard",
    "i love my girlfriend",
    "im gonna start ripping off other instagram accs",
    "i wish i could be with the humans",
    "you are loved",
    "why is meming so hard",
    "so funny xd",
]
hashtags = "#meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp"
meme_index = ["dankmeme", "meme", "bpt"]
meme_and_bpt = [meme_index[1], meme_index[2]]
dankmeme_bpt = [meme_index[0], meme_index[2]]
dankmeme_meme = [meme_index[0], meme_index[1]]


"""--------------------------- Very messy but basically used to write to a .txt file the # of meme that I'm on (ie 1, 2, etc) so the script doesn't repeat post --------------------------------------------------------------------------------------"""

memenum = 1
memenum_default = 1

with open("meme.txt", "r") as f:
    f_content = f.read()

memenum = int(float(f_content))

if memenum > 10:
    memenum = 1
else:
    memenum = int(f_content)

newmemenum = int(memenum) + 1


"""------------------------------------- Posting photo from instapy ------------------------------------------------------------------------------------------------"""
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pprint import pprint as pp
from time import sleep

from instapy import InstaPy


import autoit
import time

e = sys.exit

home = os.path.dirname(sys.argv[0])
if not home or not home.strip("."):
    home = os.path.dirname(os.path.abspath(__file__))


# INSTA_USER  = os.environ.get('INSTA_USER')
# INSTA_PWD 	= os.environ.get('INSTA_PWD')

import traceback

try:
    import cStringIO
except ImportError:
    import io as cStringIO


session = InstaPy(username=INSTA_USERNAME, password=INSTA_PASSWORD)
session.login()

phototext = "hello world!! #mom #meme"
for i in range(13):
    memenum = 1
    memenum_default = 1

    with open("meme.txt", "r") as f:
        f_content = f.read()

    memenum = int(float(f_content))

    if memenum > 13:
        memenum = 1
    else:
        memenum = int(float(f_content))

    newmemenum = int(memenum) + 1
    if memenum not in list(dankmeme_dict.values()):
        photo_path = "C:\\insta\\YOUR DIR" + str(memenum) + ".jpg"
        if memenum not in list(meme_dict.values()):
            photo_path = "C:\\insta\\YOUR DIR" + str(memenum) + ".jpg"
            if memenum not in list(bpt_dict.values()):
                photo_path = "C:\\insta\\YOUR DIR" + str(memenum) + ".jpg"
    else:
        photo_path = "C:\\insta\\YOUR DIR" + str(memenum) + ".jpg"

    caption = (
        random.choice(caption_phrases)
        + " #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp"
    )

    sleep(5)

    upload(session.browser, caption, photo_path)
    print("\nPOST SUBMITTED\n")
    with open(
        "meme.txt", "w"
    ) as file:  # writes to .txt file the # meme so the scipt remembers for next run
        file.write(str(newmemenum))

    print("NEW MEME# = ", newmemenum)


sys.exit()
