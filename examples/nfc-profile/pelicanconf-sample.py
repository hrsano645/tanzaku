# NFCプロフィール機能を使用するためのPelican設定サンプル

from datetime import datetime

# 基本設定
AUTHOR = "Your Name"
SITENAME = "Your Site Name"
SITEURL = ""
SITEDESCRIPTION = "あなたのサイトの説明"

# 言語・タイムゾーン設定
TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "ja"
DEFAULT_DATE_FORMAT = "%Y-%m-%d(%a)"

# ページネーション
DEFAULT_PAGINATION = 10
SLUGIFY_SOURCE = "basename"
SUMMARY_MAX_LENGTH = 30

# コンテンツパス
PATH = "blogbody"

# URL設定
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# テーマ設定
THEME = "./themes/tanzaku/"

# プラグイン設定
PLUGIN_PATHS = ["./pelican-plugins"]
PLUGINS = ["sitemap", "extract_toc"]

# サイトマップ設定
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# マークダウン設定
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "pymdownx.tilde": {"delete": True},
        "pymdownx.magiclink": {},
        "markdown.extensions.toc": {"title": "目次"},
    },
    "output_format": "html5",
}

# フィード設定（開発時は無効）
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# 静的ファイル設定
ARTICLE_EXCLUDES = ["extra", "before2022urlrule"]

STATIC_PATHS = [
    "images",
    "extra/",
]

EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/myblog-logo.png": {"path": "myblog-logo.png"},
    "extra/myblog-default-eyecache.png": {"path": "myblog-default-eyecache.png"},
}

# テーマ設定

# SNSリンク設定（NFCプロフィールページ内でも使用可能）
SOCIAL = (
    ("Twitter-X", "http://twitter.com/your_username"),
    ("GitHub", "https://github.com/your_username"),
    ("LinkedIn", "https://linkedin.com/in/your-profile"),
)

# OGP用デフォルト画像
DEFAULT_OG_IMAGE_URL = "/myblog-default-eyecache.png"

# コピーライト
COPYRIGTH = f"&copy; {datetime.now():%Y} {SITENAME} All rights reserved."

# サイトロゴ
SITELOGO_IMGPATH = "/myblog-logo.png"

# Pygmentsスタイル
PYGMENTS_STYLE = "paraiso-dark"

# メニュー表示設定
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
SHOW_ARTICLE_CATEGORY = True

# NFCプロフィール用追加設定（オプション）
# プロフィールページ専用の設定がある場合はここに追加

# 例: プロフィールページのメタデータ
PROFILE_CONFIG = {
    "name": "山田 太郎",
    "title": "ソフトウェアエンジニア / デザイナー",
    "motto": "テクノロジーで世界をより良い場所に",
    "avatar_url": "https://placehold.jp/150x150/4A90E2/ffffff?text=Your%20Photo",
    "qr_code_url": "https://placehold.jp/24/cccccc/333333/200x200.png?text=QR%20Code",
    "social_links": {
        "x": "https://x.com/your_username",
        "github": "https://github.com/your_username",
        "email": "your.email@example.com",
        "linkedin": "https://linkedin.com/in/your-profile",
    }
}