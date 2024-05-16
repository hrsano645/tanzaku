#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Your Name'
SITENAME = 'Your Site name'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Python.jp', 'http://python.jp/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# add theme path
THEME = "please theme path"

#----- theme configure -----#

# ABOUT_ME, EXTERNAL_AREA_**はhtmlタグなどを入れてブログパーツ的な物をいれることができます。（ご利用は計画的に）
ABOUT_ME = """
ブログについて簡単な説明が書けます
"""

EXTERNAL_AREA_SIDE_1 ="""
サイドバーの最後から一つ上に挿入されます
"""

EXTERNAL_AREA_SIDE_2 = """
サイドバーの最後に挿入されます
"""

EXTERNAL_AREA_ARTICLE_TOP = """
ブログ記事の一番上に挿入されます
"""

EXTERNAL_AREA_ARTICLE_BOTTOM = """
ブログ記事の一番下に挿入されます
"""

# demo: https://pygments.org/demo/
PYGMENTS_STYLE = "paraiso-dark"

#google custom search: by https://cse.google.co.jp/
#GOOGLE_CUSTOM_SEARCH_ID = ""