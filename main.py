import json
from facebook_scraper import get_posts


def search(string, querry):
    a = string.lower()

    if a.find(querry) >= 1:
        print("gefunden")
        print(string.encode("utf-8"))


for post in get_posts('zeremonienmeister.dold', pages=2, credentials=['Jasoninator@web.de', 'Gitarre125040708']):
    try:
        print(post)
        search(post['text'], "live")
    except:
        print("FEHLER")
