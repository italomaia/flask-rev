# Flask-Rev

Flask-Rev is a very simple flask extension that aims to make it easier to integrate
flask and those fancy reactive javascript front-ends out there (react, angular, vuejs...).
 It allows you to keep an aggressive cache with your HTTP server **AND** always return fresh
 static content to user requests. It does so by appending the static file hash to the static 
 file's url as a query string parameter. 
 
 Notice that appending the hash only happens when debug mode is False. Also, be aware
  that the hash cache is created during runtime. So, you may experience some
  "warming up" slow-down in the first request. This behavior might change in the 
  future.
 
 **The advantage of this approach**? Your static files
 names won't change between updates.

This plugin is heavely based upon these two snippets:

* https://gist.github.com/mfenniak/2978805
* https://gist.github.com/Ostrovski/f16779933ceee3a9d181#file-flask_static_files_cache_invalidator-py-L20

Thanks!

## Installation

pip install flask-rev

## Usage
```
from flask import Flask, url_for
from flask_rev import Rev

app = Flask(__name__)
Rev(app)

url_for('static', filename='bundle.js')
# outputs: /static/bundle.js?h=<md5hash>
```
