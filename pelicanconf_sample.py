from datetime import datetime

AUTHOR = "[your name]"
SITENAME = ""
SITEURL = ""
SITEDESCRIPTION = ""

TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "ja"
DEFAULT_DATE_FORMAT = "%Y-%m-%d(%a)"

PATH = "content"

# URL, SaveAs
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# other config
DEFAULT_PAGINATION = 10
SLUGIFY_SOURCE = "basename"
SUMMARY_MAX_LENGTH = 30


# theme directory
THEME = "./themes/tanzaku/"

# plugins
# PLUGIN_PATHS = ["pelican-plugins"]
# PLUGINS = ["sitemap", "extract_toc"]

# pulgins config: sitemap
# SITEMAP = {
#     "format": "xml",
#     "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
#     "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
# }

# plugins config: markdown
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "pymdownx.tilde": {},
        "pymdownx.magiclink": {},
        "markdown.extensions.toc": {"title": "ToC"},
    },
    "output_format": "html5",
}

# Feed generation is usually not desired when developing
# FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# static files... (favicon, robots.txt)
ARTICLE_EXCLUDES = ["extra"]

# STATIC_PATHS = [
#     "images/",
#     "extra/",
# ]

# EXTRA_PATH_METADATA = {
#     "extra/robots.txt": {"path": "robots.txt"},
#     "extra/favicon.ico": {"path": "favicon.ico"},
# }

# [THEME CONFIG]
COPYRIGTH = f"&copy; {datetime.now():%Y} {SITENAME} All rights reserved."

# DEFAULT_OG_IMAGE_URL = ""
# SITELOGO_SVGTAG = ""
# SITELOGO_IMGPATH = ""

# index header
# HEADER_INNER = {
#     "title": SITENAME,
#     "message": SITEDESCRIPTION,
# }

# navbar menu
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
SHOW_ARTICLE_CATEGORY = True

# Social icon: need change
SOCIAL = (
    ("Twitter-X", "http://twitter.com/hrs_sano645"),
    ("Facebook", "https://www.facebook.com/hrs.sano645"),
    ("Github", "https://github.com/hrsano645"),
    # ("Instagram", ""),
    # ("YouTube", ""),
)
