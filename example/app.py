import sys
from flask import url_for
from flask import Flask
from flask import Blueprint
from blog.app import blog


# so we can see the module without installing
sys.path.append('../')

from flask_rev import Rev


app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost'
app.register_blueprint(blog)
rev = Rev(app)

with app.test_request_context('/'):
    print(url_for('static', filename='style.css'))
    print(url_for('blog.static', filename='style.css'))
