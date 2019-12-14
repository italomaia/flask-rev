"""
Flask-Rev
-------------

Extension that adds file hash to static files
url.
"""
from setuptools import setup


setup(
    name='Flask-Rev',
    version='0.1.2',
    url='https://github.com/italomaia/flask-rev',
    license='BSD',
    author='Italo Maia',
    author_email='italo.maia@gmail.com',
    description='Easily integrate flask with revisioned static files',
    long_description=__doc__,
    py_modules=['flask_rev'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_rev'],
    test_suite='tests.test_rev',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
