from app import app
from flask import request, abort, jsonify
from threading import Thread

from scrapers.insta_scraper import insta_scrape
from scrapers.yt_scraper import get_channel_info
from scrapers.twitch_scraper import twtich_scrape
from scrapers.tweet_scraper import twitter_scrape
from scrapers.reddit_scraper import reddit_scrape
from scrapers.so_scraper import so_scraper

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return
 
scrapers = [twtich_scrape, twitter_scrape, insta_scrape, reddit_scrape, get_channel_info, so_scraper]
names = ["twitch", "twitter", "instagram", "reddit", "youtube", "stack overflow"]

@app.route('/', methods=['GET', 'POST'])
def home():
    threads = []
    results = {}

    data = request.json

    username = data["username"]

    for scraper in scrapers:
        thread = ThreadWithReturnValue(target=scraper, args=(username,))
        thread.start()
        threads.append(thread)

    for i in range(len(threads)):
        res = threads[i].join()
        results[names[i]] = res
    
    return jsonify(results)

