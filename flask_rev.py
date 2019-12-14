"""
    Flask Rev
    ~~~~~~~~~

    Simple plugin that makes it easy to avoid reading old
    cached static files from the http server.
"""

from flask.helpers import safe_join
from flask import request
import hashlib
import contextlib


class Rev(object):
    """
    Patches url_for function for the .static endpoint.
    """

    def __init__(self, app=None):
        """
        If app is provided, initializes extension.

        :param app: Flask application instance
        :type app: flask.Flask
        """
        self._file_hash_cache = {}
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Initializes extension with app

        :param app: Flask application instance
        :type app: flask.Flask
        """
        if app.debug:  # don't mess with debug
            return

        @app.url_defaults
        def hashed_url_for_static_file(endpoint, values):
            if 'static' == endpoint or endpoint.endswith('.static'):
                filename = values.get('filename')
                if filename:
                    # has higher priority
                    blueprint = endpoint.rsplit('.', 1)[0] \
                        if '.' in endpoint else request.blueprint

                    # file from blueprint or project?
                    static_folder = app.blueprints[blueprint].static_folder \
                        if blueprint else app.static_folder

                    # avoids querystring key collision
                    param_name = 'h'
                    while param_name in values:
                        param_name = '_' + param_name

                    filepath = safe_join(static_folder, filename)
                    values[param_name] = self.get_file_hash(filepath)

    def get_file_hash(self, filepath):
        """
        Returns file hash from cache.

        :param filepath: path to static file
        :type filepath: str
        """
        if filepath not in self._file_hash_cache:
            self._file_hash_cache[filepath] = self.static_file_hash(filepath)
        return self._file_hash_cache[filepath]

    @staticmethod
    def static_file_hash(filepath):
        """
        Calculates file hash. Uses md5 algorithm.

        :param filepath: path to static file
        :type filepath: str
        """
        hasher = hashlib.md5()  # nosec: B303

        with contextlib.closing(open(filepath, 'rb')) as file:
            hasher.update(file.read())
        return hasher.hexdigest()
