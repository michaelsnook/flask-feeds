import os
from dotenv import load_dotenv
from textwrap import dedent

load_dotenv()

# Bluesky username
HANDLE = os.getenv('BLUESKY_USERNAME')

# Bluesky app password, available via: https://bsky.app/settings/app-passwords
PASSWORD = os.getenv('BLUESKY_APP_PASSWORD')

# Domain where the feed is hosted
SERVICE_DOMAIN = "flask-feeds.vercel.app"

# Feed Details

# A short name for the record that will show in urls
# Lowercase with no spaces.
# Ex: whats-hot
RECORD_NAME: str = "indiasky"

# A display name for your feed
# Ex: What's Hot
DISPLAY_NAME: str = "IndiaSky"

# (Optional) A description of your feed
# Ex: Top trending content from the whole network
DESCRIPTION: str = dedent(
    """
    India posters!
    """
).strip()

SERVICE_DID = f"did:web:{SERVICE_DOMAIN}"

# Feed URI generated by running `python setup_feed.py`
FEED_URI = ""

# Skyfeed path
SKYFEED_DID = "did:plc:4yawo46bsobbzd55b7uxdvmo/feed/aaacjfe2xhorq"

SKYFEED_PATH = f"at://{SKYFEED_DID}".replace(
    "/feed/", "/app.bsky.feed.generator/")
