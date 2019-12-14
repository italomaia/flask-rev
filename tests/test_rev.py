from __future__ import with_statement

import sys

from flask import Flask, url_for
from flask_rev import Rev


if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class RevTestCase(unittest.TestCase):

    def init_app(self, debug):
        app = self.app = Flask(__name__)
        app.debug = debug
        Rev(app)

    def test_plain_url_for(self):
        self.init_app(False)
        with self.app.test_request_context():
            uri = url_for('static', filename='example.css')
            expected = '/static/example.css?h=981e0d36a18745ecf9607812379348ff'
            self.assertEqual(uri, expected)

    def test_does_nothing_in_debug_mode(self):
        self.init_app(True)
        with self.app.test_request_context():
            uri = url_for('static', filename='example.css')
            self.assertEqual(uri, '/static/example.css')
