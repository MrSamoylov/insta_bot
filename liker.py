# -*- coding: utf-8 -*-
import argparse
import os
import pprint
from insta_browser import browser

SCRIPT_PATH = os.path.dirname(__file__)
COOKIE_PATH = '{}/var/cookie'.format(SCRIPT_PATH)
SCREEN_SHOT_PATH = '{}/var/screenshot'.format(SCRIPT_PATH)
LOGGER_FILE = '{}/var/log/insta_browser.txt'.format(SCRIPT_PATH)

parser = argparse.ArgumentParser()
parser.add_argument('--debug', help='enable debug mode', action="store_true")
parser.add_argument('--chrome', help='using Chrome webdriver instead of PhantomJS', action="store_true")
parser.add_argument('--count', help='if indicated, like posts by count', type=int, default=0)
args = parser.parse_args()
debug = args.debug
chrome = args.chrome
count = args.count


login = os.environ.get('insta_login')
password = os.environ.get('insta_password')

exclude = open('{}/var/exclude_accounts.txt'.format(SCRIPT_PATH)).read().split(',')

br = browser.Browser(debug, chrome, COOKIE_PATH, SCREEN_SHOT_PATH, LOGGER_FILE, exclude)
try:
    br.auth(login, password)
    if count:
        br.scroll_feed_by_posts_count(count)
    else:
        br.scroll_feed_to_last_not_liked_posts()
    br.like_found_posts()
finally:
    print(br.get_summary())
    br.close_all()