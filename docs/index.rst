Flask-Rev
=========

.. module:: flask_rev

Flask-Rev is an extension to `Flask` that makes it easy
to avoid cache invalidation problems that happens when you
have a aggressive cache police for your **static files**.

How it works
------------

Flask Rev patches url_for in a manner that, whenever
you construct a url for a static file, it appends the
file's hash to the end of the url. This way, your static
file server will receive a different request whenever
the static file is changed.

Also, be aware that flask-rev does *nothing* in debug
mode. This might change to something configurable, but
of now, this is how it is.

Installation
------------

**Pi**m**p** your way up::

  $ pip install Flask-Rev

How to Use
----------

Just initialize the extension and you're ready to go::

  from flask.rev import Rev
  Rev(app)

Changes
-------

0.1.1
```

-   MVP is ready.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
