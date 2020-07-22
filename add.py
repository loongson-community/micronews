#!/usr/bin/python3
# 2016-08-01: Initial script. Ana Guerrero Lopez <ana@debian.org>
# IMPORTANT: The timezone is always Europe/Paris because it must match
# the timezone used in pelicanconf.py
# GPL v2 or any later


import argparse
import calendar
import time
import os
import re
import shlex
import subprocess

re_link = re.compile(r'(https?://\S+)')
base_dir = os.path.abspath(os.path.dirname(__file__))

parser = argparse.ArgumentParser(description="Add a dent for micronews")

parser.add_argument('-a', action="store", help="Your name",
                    default=os.environ.get('DEBFULLNAME', ''))
parser.add_argument('-t', action="store", required=True, help="Text you want to submit")
parser.add_argument('-y', default=False, action='store_true', help="Skip confirmation")
args = parser.parse_args()
if not args.a:
    parser.error("You must specify your name via '-a' or via the DEBFULLNAME "
                 "environment variable")

title = args.t
# content needs the links in markdown
content = re_link.sub(r'[\g<1>](\g<1>)', args.t)
author = args.a

if not content:
    parser.error("Refusing to accept empty title.")

# Prevent issues like <https://twitter.com/debian/status/997445202838081536>
if len(re_link.findall(args.t)) > 1:
    parser.error("Refusing to accept title with multiple URIs as dlvr.it will "
                 "mangle them incorrectly.")

os.chdir(base_dir)
os.environ['TZ'] = "Asia/Shanghai"
time.tzset()
now = time.localtime()
now_epoch = calendar.timegm(now)
now_human = time.strftime("%Y-%m-%d %H:%M", now)

dent = """Title: {}
Slug: {}
Date: {}
Author: {}
Status: published

{}
""".format(title, now_epoch, now_human, author, content)

dent_dir = "content/{}/{}/".format(time.strftime("%Y"), time.strftime("%m"))
# Create the directory for the new month
if not os.path.exists(dent_dir):
    os.makedirs(dent_dir)

dent_file = os.path.join(dent_dir, '{}.md'.format(now_epoch))
with open(dent_file, "w") as f:
    f.write(dent)

cmds = (
    'git add {}'.format(dent_file),
    'git commit -m "{}"'.format('New post ' + str(dent_file)),
)

print("""
Please commit your changes and push by running the following commands:

{}
""".format('\n'.join(cmds)))

try:
    if args.a == True or input("Do you want to run this now? [y/N] ").strip().lower() == 'y':
        for x in cmds:
            subprocess.check_call(x, shell=True)
except KeyboardInterrupt:
    sys.exit(2)
