from pushbullet import Pushbullet
import requests
from bs4 import BeautifulSoup

def check_for_update():
    API_KEY = "o.XDaXmpNIpR1nNM2fMVNw8mXmXr1YiPB6"
    file_name = "previous.txt"

    file = open(file_name, "r+")
    text = file.read()

    pb = Pushbullet(API_KEY)
    URL = "https://w4.onepunch-manga.com/"
    r = requests.get(URL)

    soup = BeautifulSoup(r.text, features="html.parser")
    last_episode = soup.find(class_="su-post")
    title = last_episode.a.string
    if text == title:
        pb.push_note('Nothing ...', 'No new chapter today')
    else:
        pb.push_note('New Chapter!!!', title)
        file.seek(0)
        file.truncate()
        file.write(title)
    file.close()


if __name__ == '__main__':
    check_for_update()
