#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# Basic details
AUTHOR = 'Loongson Community'
SITENAME = 'Loongson micronews'
# This is only required in publishconf.py
SITEURL = 'https://loongson-community.github.io/micronews'
PATH = 'content'
OUTPUT_PATH = 'output/'

# Configuration
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'en'
DELETE_OUTPUT_DIRECTORY = True
THEME = "theme-micro"
DEFAULT_PAGINATION =10
DISPLAY_PAGES_ON_MENU = True
SUMMARY_MAX_LENGTH = None
LOCALE='C'

# URL settings
RELATIVE_URLS = True
ARTICLE_URL = '{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'

# Do not create author pages
AUTHORS_SAVE_AS = None
AUTHOR_SAVE_AS = ''
AUTHOR_URL = ''

# Do not create tag pages
TAGS_SAVE_AS = None
TAG_SAVE_AS = ''
TAG_URL = None

# Do not create category pages
CATEGORIES_SAVE_AS = None
CATEGORY_SAVE_AS = ''
CATEFORY_URL = None

# Create month and year archives
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Feeds settings
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/feed.rss'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None


MENUITEMS =  ()
SOCIAL = ()

PATH = 'content'
STATIC_PATHS = [
    'extras/favicon.ico',
	'images',
    ]
EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path': 'favicon.ico'},
    }
