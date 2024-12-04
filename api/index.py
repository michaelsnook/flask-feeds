from flask import Flask
from atproto import Client
from api.services.user_management import add_user_to_list
from itertools import compress
from datetime import datetime, timezone
from tqdm.contrib.concurrent import thread_map
import api.config as config


app = Flask(__name__)


def parse_date(date_string):
    return datetime.fromisoformat(date_string.replace("Z", "+00:00"))


def hackernews_score(item, gravity: float = 2.5):
    hours_passed = (
        datetime.now(timezone.utc) - parse_date(item.post.indexed_at)
    ).total_seconds() / 3600

    points = (
        item.post.like_count
        + item.post.quote_count
        + item.post.reply_count
        + item.post.repost_count
    )
    score = points / ((hours_passed + 2) ** (gravity))
    return score


def rank_posts(feed):
    # return sorted(feed, key=lambda item: parse_date(item.post.indexed_at), reverse=True)
    return sorted(feed, key=hackernews_score, reverse=True)


def fetch_latest_posts():
    client = Client()
    client.login(config.HANDLE, config.PASSWORD)

    data = client.app.bsky.feed.get_feed(
        {
            "feed": config.SKYFEED_PATH,
            "limit": 100,
        },
        timeout=100,
    )

    feed = data.feed
    for _ in range(2):
        data = client.app.bsky.feed.get_feed(
            {"feed": config.SKYFEED_PATH, "limit": 100, "cursor": data.cursor},
            timeout=200,
        )
        feed.extend(data.feed)

    sorted_feed = rank_posts(feed)
    post_uris = [item.post.uri for item in sorted_feed]
    return post_uris


@app.route('/feeds/indiasky')
def home():
    post_uris = fetch_latest_posts()
    feed_skeleton = {"feed": [{"post": uri} for uri in post_uris]}
    return feed_skeleton


@app.route('/feeds/about')
def about():
    return 'About'

@app.route('/add_user_to_list', methods=['POST'])
def add_user():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.json
        list_uri = data.get('list_uri')
        user_did = data.get('user_did')
        
        if not list_uri or not user_did:
            return jsonify({'error': 'Missing list_uri or user_did'}), 400
        
        result = add_user_to_list(user_did, list_uri)
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Content-Type not supported'}), 415