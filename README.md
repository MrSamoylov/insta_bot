## Requirements
* python 3
* virtualenv
* chrome or phantomJS web driver

## Installation:
```
virtualenv env -p $(which python3) --no-wheel --no-setuptools
env/bin/pip install -r requirements.txt
```

Download and place binary from archive to bin folder - http://phantomjs.org/download.html

## Upgrade
After each `git pull` run command to update packages from requirements:   
`env/bin/pip install -r requirements.txt --upgrade`

## Usage
run liker
```
insta_login=yourInstaLogin insta_password=yourInstaPassword env/bin/python liker.py
--debug  - for console log
--chrome - for using Chrome webdriver instead of PhantomJS
--count 10 - for liking just 10 posts from feed
```

liker will like all posts from your feed until last unliked