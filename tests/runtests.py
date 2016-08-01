from __future__ import with_statement

import sys

from flask import Flask, url_for
from flask_rev import Rev

if sys.version_info < (2,7):
    import unittest2 as unittest
else:
    import unittest


class CacheTestCase(unittest.TestCase):

    def setUp(self):
        app = self.app = Flask(__name__)
        app.debug = False
        self.rev = Rev(app)

    def test_plain_url_for(self):
        with self.app.test_request_context():
            uri = url_for('static', filename='example.css')
            self.assertEqual(uri, '/static/example.css?h=981e0d36a18745ecf9607812379348ff')


if __name__ == '__main__':
    unittest.main()