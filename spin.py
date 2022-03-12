from pushbullet import Pushbullet
import requests, time
from bs4 import BeautifulSoup

API_KEY = "o.XDaXmpNIpR1nNM2fMVNw8mXmXr1YiPB6"

pb = Pushbullet(API_KEY)
URL = "https://w4.onepunch-manga.com/"
r = requests.get(URL)

soup = BeautifulSoup(r.text, features="html.parser")
last_episode = soup.find(class_="su-post")
title = last_episode.a.string

while True:
    time.sleep(900)
    soup = BeautifulSoup(r.text, features="html.parser")
    last_episode = soup.find(class_="su-post")
    new_title = last_episode.a.string

    if new_title != title:
        pb.push_note('New Chapter!!!', title + '\n' + URL)
        title = new_title



