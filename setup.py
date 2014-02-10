# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import OrderTracker
version = OrderTracker.__version__

setup(
    name='OrderTracker',
    version=version,
    author='',
    author_email='osterallen@gmail.com',
    packages=[
        'OrderTracker',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['OrderTracker/manage.py'],
)