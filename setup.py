#!/usr/bin/env python
from setuptools import setup

setup(
    name='django-taxonomy',
    version='0.1.0',
    description='A flexible taxonomy approach for Django.',
    author="Mike O'Malley",
    author_email='spuriousdata@gmail.com',
    url='http://github.com/spuriousdata/django-taxonomy',
    packages=[
        'taxonomy',
        'taxonomy.templatetags',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License'
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
