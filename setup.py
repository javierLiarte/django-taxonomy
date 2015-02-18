#!/usr/bin/env python
from setuptools import setup

setup(
    name='django-taxonomy',
    version='0.1.0',
    description='A flexible taxonomy approach for Django.',
    author="Javier Liarte, Mike O'Malley, ShadowKyogre, Brian K. Jones",
    author_email='jliarte@gmail.com',
    url='http://github.com/javierLiarte/django-taxonomy',
    install_requires=[
        'django_mptt_admin>=0.2.0',
        'django-mptt>=0.6.1',
    ],
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
