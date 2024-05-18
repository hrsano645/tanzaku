import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = ""
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
# CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

RSS_FEED_SUMMARY_ONLY = False
DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
DISQUS_SITENAME = ""
DISQUS_SITEURL = SITEURL
ANALYTICS = """"""

# google custom search: by https://cse.google.co.jp/
GOOGLE_CUSTOM_SEARCH_ID = ""
