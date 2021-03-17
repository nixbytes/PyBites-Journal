from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    feeds = feedparser.parse(FEED_URL)
    GameTotal = []
    for feed in feeds.entries:
        title = feed['title']
        feed_links = feed['link']
        GameTotal.append(Game(title,feed_links))
    return GameTotal
